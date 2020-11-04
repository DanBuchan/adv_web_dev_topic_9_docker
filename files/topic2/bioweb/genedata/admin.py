from django.contrib import admin
from .models import *


class GeneAttributeLinkInline(admin.TabularInline):
    model = GeneAttributeLink
    extra = 3


class GeneAdmin(admin.ModelAdmin):
    list_display = ('gene_id', 'entity', 'start', 'stop', 'sense')
    inlines = [GeneAttributeLinkInline]


class ECAdmin(admin.ModelAdmin):
    list_display = ('ec_name', )


class SequencingAdmin(admin.ModelAdmin):
    list_display = ('sequencing_factory', 'factory_location')


admin.site.register(Gene, GeneAdmin)
admin.site.register(EC, ECAdmin)
admin.site.register(Sequencing, SequencingAdmin)
