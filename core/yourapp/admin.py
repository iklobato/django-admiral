from django.contrib import admin

from .models import AllFieldTypes

FIELDS = (
    'integer_field',
    'positive_integer',
    'small_integer',
    'big_integer',
    'decimal_field',
    'float_field',
)

@admin.register(AllFieldTypes)
class AllFieldTypesAdmin(admin.ModelAdmin):
    list_display = FIELDS
    list_filter = FIELDS
    search_fields = FIELDS

    class Media:
        css = {'all': ('admin/css/custom_admin.css',)}
        js = ('admin/js/custom_admin.js',)

