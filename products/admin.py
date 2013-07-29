# coding=utf-8
from decimal import Decimal
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
        'price',
        'get_sum',
        'user',
    ]
    readonly_fields = ['get_week_day', 'get_sum']
    list_filter = [
        'product__name',
        'sex__name',
        'size__name',
        'color__name',
        'imprint__name',
        'user__username',
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
                'price',
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

        if sale.number and sale.price:
            sale_sum = Decimal(sale.price.price) * sale.number
            if sale.employee_discount:
                sale_sum /= 2
            return '<strong>%s€</strong>' % sale_sum
        return '-'
    get_sum.short_description = 'Summe'
    get_sum.allow_tags = True


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
        'product__name',
        'delivery_date',
    ]
    actions = None


admin.site.register(Sex)
admin.site.register(Size)
admin.site.register(Product)
admin.site.register(Imprint)
admin.site.register(Price)
admin.site.register(Color)
admin.site.register(Sale, SaleAdmin)
admin.site.register(Delivery, DeliveryAdmin)
