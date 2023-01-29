from django.contrib import admin

from shop.models import *

# Register your models here.
class catadmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
admin.site.register(category,catadmin)
class Itemadmin(admin.ModelAdmin):
    list_display = ['Item_name','Item_slug','Item_cat','Item_desc','Item_price']
    list_editable = ['Item_desc','Item_price']
    prepopulated_fields = {'Item_slug':('Item_name',)}
admin.site.register(Items,Itemadmin)

admin.site.register(Cart)
admin.site.register(Profile)

