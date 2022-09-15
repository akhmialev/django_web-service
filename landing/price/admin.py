from django.contrib import admin
from price.models import PriceTable, PriceCard


class PriceAdmin(admin.ModelAdmin):
    list_display = ('pc_value', 'pc_description')


admin.site.register(PriceCard, PriceAdmin)
admin.site.register(PriceTable)
