# coding=utf-8
from datetime import datetime
from django.core.cache import cache
from products.models import Sale


def sales_sum(request):

    sales_sum = cache.get('sales_sum')

    if not sales_sum:
        sales_sum = Sale.data.get_sum_for_current_year()
        cache.set('sales_sum', sales_sum, 60*60)

    return {'sales_sum': sales_sum, 'sales_year': datetime.now().year}
