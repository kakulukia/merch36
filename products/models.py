# coding=utf-8
from datetime import datetime, date
from decimal import Decimal
from django.contrib.auth.models import User
from django.core.cache import cache
from django.db import models


# basic model stuff
##########################################
from django.db.models import Sum
from django.forms import forms
from smart_selects.db_fields import ChainedForeignKey


class BaseDataManager(models.Manager):

    def get_query_set(self):
        qs = super(BaseDataManager, self).get_query_set()
        return qs.filter(active=True)


class BaseModelManagerAll(models.Manager):

    def deleted(self):
        return self.filter(active=False)


# Create your models here.
class BaseModel(models.Model):

    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True, editable=False)

    active = models.BooleanField(default=True, editable=False)

    # access only active data
    data = BaseDataManager()
    # access all data
    objects = BaseModelManagerAll()

    class Meta:
        abstract = True
        ordering = ['-created']

    # deleted data is bad - doing it you shouldn't!
    def delete(self, using=None):
        self.active = False
        self.save()


class NamedModel(models.Model):
    name = models.CharField('Name', max_length=150)

    class Meta:
        ordering = ['name']
        abstract = True

    def __unicode__(self):
        return self.name


# actual models for the project
class Product(BaseModel, NamedModel):

    sizes = models.ManyToManyField('Size', verbose_name=u'Größen')
    sexes = models.ManyToManyField('Sex', verbose_name='Sex')
    colors = models.ManyToManyField('Color', verbose_name='Farben')

    price = models.ForeignKey('Price', verbose_name='Preis')
    employee_price = models.ForeignKey('Price', verbose_name='Mitarbeiter-Preis',
                                       related_name='employee_products')

    class Meta:
        verbose_name = 'Produkt'
        verbose_name_plural = 'Produkte'


class Sex(BaseModel, NamedModel):

    class Meta:
        verbose_name = 'Sex'
        verbose_name_plural = 'Sex'


class Size(BaseModel, NamedModel):
    value = models.IntegerField(u'Größe')

    class Meta:
        ordering = ['value']
        verbose_name = u'Größe'
        verbose_name_plural = u'Größen'


class Color(BaseModel, NamedModel):
    class Meta:
        verbose_name = 'Farbe'
        verbose_name_plural = 'Farben'


class Imprint(BaseModel, NamedModel):
    class Meta:
        verbose_name = 'Aufdruck'
        verbose_name_plural = 'Aufdrucke'


class Price(BaseModel):
    price = models.IntegerField('Preis-Klasse')

    class Meta:
        ordering = ['price']
        verbose_name = 'Preis'
        verbose_name_plural = 'Preise'

    def __unicode__(self):
        return unicode(u'%s€' % self.price)


class SalesManager(BaseDataManager):

    def get_sum_for_current_year(self):
        sales_sum = cache.get('sales_sum')

        if not sales_sum:
            sales_sum = Decimal()
            for s in self.filter(created__gte=date(datetime.now().year, 1, 1)).prefetch_related('product'):
                if s.employee_discount:
                    cur_sum = Decimal(s.product.employee_price.price) * s.number
                else:
                    cur_sum = Decimal(s.product.price.price) * s.number
                sales_sum += cur_sum
            cache.set('sales_sum', sales_sum, 60*60)

        return sales_sum


class Sale(BaseModel):
    product = models.ForeignKey(Product, verbose_name='Produkt')
    sex = ChainedForeignKey(
        Sex,
        chained_field="product",
        chained_model_field="product",
        show_all=False,
        auto_choose=True
    )
    size = ChainedForeignKey(
        Size,
        chained_field="product",
        chained_model_field="product",
        show_all=False,
        auto_choose=True
    )
    color = ChainedForeignKey(
        Color,
        chained_field="product",
        chained_model_field="product",
        show_all=False,
        auto_choose=True
    )
    imprint = models.ForeignKey(Imprint, verbose_name='Aufdruck')
    purchase_date = models.DateField('Datum')
    employee_discount = models.BooleanField('Mitarbeiter-Rabatt')
    number = models.IntegerField('Anzahl')

    user = models.ForeignKey(User, verbose_name='Mitarbeiter', editable=False)
    notes = models.TextField('Notizen', blank=True, null=True)

    data = SalesManager()

    class Meta:
        ordering = ['-purchase_date']
        verbose_name = 'Verkauf'
        verbose_name_plural = u'Verkäufe'

    def __unicode__(self):
        return u'%s - %sx %s' % (self.purchase_date, self.number, self.product)

    def clean(self):
        if self.sex and self.size and self.product and\
                self.color and self.imprint and self.number:

            # calculate storage numbers
            deliveries = Delivery.data.filter(
                product=self.product,
                size=self.size,
                sex=self.sex,
                color=self.color,
                imprint=self.imprint
            )
            sales = Sale.data.filter(
                product=self.product,
                size=self.size,
                sex=self.sex,
                color=self.color,
                imprint=self.imprint
            )

            if self.id:
                sales = sales.exclude(id=self.id)

            items_in_store = deliveries.aggregate(sum=Sum('number'))['sum'] if deliveries else 0
            items_sold = sales.aggregate(sum=Sum('number'))['sum'] if sales else 0

            if items_sold + self.number > items_in_store:
                raise forms.ValidationError(
                    u'Nicht geügend Ware vorhanden (%s)! '
                    u'Bitte vorher die Lieferungen aufnehmen.' % (items_in_store - items_sold))


class Delivery(BaseModel):

    delivery_date = models.DateField('Lieferdatum')

    product = models.ForeignKey(Product, verbose_name='Produkt')

    sex = ChainedForeignKey(
        Sex,
        chained_field="product",
        chained_model_field="product",
        show_all=False,
        auto_choose=True
    )
    size = ChainedForeignKey(
        Size,
        chained_field="product",
        chained_model_field="product",
        show_all=False,
        auto_choose=True
    )
    color = ChainedForeignKey(
        Color,
        chained_field="product",
        chained_model_field="product",
        show_all=False,
        auto_choose=True
    )
    imprint = models.ForeignKey(Imprint, verbose_name='Aufdruck')
    number = models.IntegerField('Anzahl')

    class Meta:
        verbose_name = 'Lieferung'
        verbose_name_plural = 'Lieferungen'
        ordering = ['-delivery_date']
