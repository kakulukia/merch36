# coding=utf-8
from django.contrib.auth.models import User
from django.db import models


# basic model stuff
##########################################
class BaseModelManager(models.Manager):

    def get_query_set(self):
        qs = super(BaseModelManager, self).get_query_set()
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
    data = BaseModelManager()
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


class Sale(BaseModel):
    product = models.ForeignKey(Product, verbose_name='Produkt')
    sex = models.ForeignKey(Sex)
    size = models.ForeignKey(Size, verbose_name=u'Größe')
    color = models.ForeignKey(Color, verbose_name='Farbe')
    imprint = models.ForeignKey(Imprint, verbose_name='Aufdruck')
    purchase_date = models.DateField('Datum')
    employee_discount = models.BooleanField('Mitarbeiter-Rabatt')
    number = models.IntegerField('Anzahl')
    price = models.ForeignKey(Price, verbose_name='Preis')

    user = models.ForeignKey(User, verbose_name='Mitarbeiter')

    class Meta:
        ordering = ['-purchase_date']
        verbose_name = 'Verkauf'
        verbose_name_plural = u'Verkäufe'

    def __unicode__(self):
        return u'%s - %sx %s' % (self.purchase_date, self.number, self.product)


class Delivery(BaseModel):

    delivery_date = models.DateField('Lieferdatum')

    product = models.ForeignKey(Product, verbose_name='Produkt')
    sex = models.ForeignKey(Sex)
    size = models.ForeignKey(Size, verbose_name=u'Größe')
    color = models.ForeignKey(Color, verbose_name='Farbe')
    imprint = models.ForeignKey(Imprint, verbose_name='Aufdruck')
    number = models.IntegerField('Anzahl')

    class Meta:
        verbose_name = 'Lieferung'
        verbose_name_plural = 'Lieferungen'
        ordering = ['-delivery_date']
