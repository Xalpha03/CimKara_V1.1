from django.contrib import admin
from .models import *

# Register your models here.


class EnsachageAdmin(admin.ModelAdmin):
    '''Admin View for '''
    
    model = EnsachageModel
    fields = ('user', 'livraison', 'casse', 'vrack', 'created')
    list_display = ('user', 'livraison', 'casse', 'ensache', 'tx_casse', 'vrack', 'created')
    
    list_filter = ('user', 'created')
    readonly_fields = ('ensache', 'tx_casse')
    search_fields = ('created', 'user')
    ordering = ('-created',)

admin.site.register(EnsachageModel, EnsachageAdmin)
