# coding=utf-8
from decimal import Decimal
from datetime import datetime
import autocomplete_light
from django.contrib import admin
from django import forms
from django.template.defaultfilters import date as date_format

from products.models import Imprint, Price, Sale, Color, Product, Size, Sex, Delivery


class SaleForm(forms.ModelForm):

    class Meta:
        model = Sale

    def clean_number(self):
        data = self.cleaned_data
        if not data['number']:
            raise forms.ValidationError('Das lohnt nicht ..')

        return data.get('number')


class SaleAdmin(admin.ModelAdmin):
    search_fields = ['product__name', 'notes']
    list_display = [
        'purchase_date',
        'get_week_day',
        'product',
        'sex',
        'size',
        'color',
        'imprint',
        'employee_discount',
        'number',
        'get_price',
        'get_sum',
        'user',
    ]
    readonly_fields = ['get_week_day', 'get_sum', 'user', 'get_price']
    list_filter = [
        'product',
        'sex',
        'size',
        'color',
        'imprint',
        'user',
        'purchase_date',
    ]
    date_hierarchy = 'purchase_date'
    actions = None

    fieldsets = (
        (None, {
            'fields': (
                'product',
                'sex',
                'size',
                'color',
                'imprint',
                'purchase_date',
                'get_week_day',
                'employee_discount',
                'number',
                'get_price',
                'get_sum',
                'user',

                'notes',
            )
        }),
    )
    form = SaleForm

    def get_week_day(self, sale):
        if not sale.purchase_date:
            return '-'
        return date_format(sale.purchase_date, 'l')
    get_week_day.short_description = 'Wochentag'

    def get_sum(self, sale):

        if sale.number and sale.product:
            if sale.employee_discount:
                sale_sum = Decimal(sale.product.employee_price.price) * sale.number
            else:
                sale_sum = Decimal(sale.product.price.price) * sale.number
            return '<strong>%s€</strong>' % sale_sum
        return '-'
    get_sum.short_description = 'Summe'
    get_sum.allow_tags = True

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context.update({
            'sales_sum': Sale.data.get_sum_for_current_year(),
            'sales_year': datetime.now().year
        })
        print 'updating'
        return super(SaleAdmin, self).changelist_view(request, extra_context=extra_context)

    def save_model(self, request, obj, form, change):
        if not obj.user_id:
            obj.user = request.user
        obj.save()

    def get_price(self, obj):
        if obj.employee_discount:
            return obj.product.employee_price
        else:
            return obj.product.price
    get_price.short_description = 'Preis'
    get_price.admin_order_field = 'product__price'


class DeliveryAdmin(admin.ModelAdmin):
    list_display = [
        'delivery_date',
        'product',
        'sex',
        'size',
        'color',
        'imprint',
        'number',
    ]
    list_filter = [
        'product',
        'delivery_date',
    ]
    actions = None


class ProductAdmin(admin.ModelAdmin):
    form = autocomplete_light.modelform_factory(Product)

admin.site.register(Sex)
admin.site.register(Size)
admin.site.register(Product, ProductAdmin)
admin.site.register(Imprint)
admin.site.register(Price)
admin.site.register(Color)
admin.site.register(Sale, SaleAdmin)
admin.site.register(Delivery, DeliveryAdmin)
