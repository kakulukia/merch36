# coding=utf-8
from django.conf.urls import patterns, include, url
import autocomplete_light

# import every app/autocomplete_light_registry.py
autocomplete_light.autodiscover()

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'merch36.views.home', name='home'),
    # url(r'^merch36/', include('merch36.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^', include(admin.site.urls)),
    url(r'^autocomplete/', include('autocomplete_light.urls')),
    url(r'^chaining/', include('smart_selects.urls')),
)
