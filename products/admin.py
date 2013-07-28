# coding=utf-8
from django.contrib import admin
from django.template.defaultfilters import date as date_format

from products.models import Imprint, Price, Sale, Color, Product, Size, Sex, Delivery


class SaleAdmin(admin.ModelAdmin):
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
        'user',
    ]
    readonly_fields = ['get_week_day']
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
                'user',
            )
        }),
    )

    def get_week_day(self, obj):
        if not obj.purchase_date:
            return '-'
        return date_format(obj.purchase_date, 'l')
    get_week_day.short_description = 'Wochentag'


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
