# coding=utf-8
import autocomplete_light
from models import Sex, Size, Color


autocomplete_light.register(
    Sex,
    search_fields=['^name'],
    autocomplete_js_attributes={
        'minimum_characters': 0,
        'placeholder': u'Sex ..',
    },
)
autocomplete_light.register(
    Size,
    search_fields=['^name'],
    autocomplete_js_attributes={
        'minimum_characters': 0,
        'placeholder': u'Größe ..',
    },
)
autocomplete_light.register(
    Color,
    search_fields=['^name'],
    autocomplete_js_attributes={
        'minimum_characters': 0,
        'placeholder': u'Farbe ..',
    },
)
