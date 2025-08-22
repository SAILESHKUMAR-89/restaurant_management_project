from django.contrib import admin
from .models import Item, Menu
from .models import RestaurantLocation

# Custom Admins
class ItemAdmin(admin.ModelAdmin):
    list_display = ['item_name','item_price','created_at']
class MenuAdmin(admin.ModelAdmin):
    list_display = ("name", "price")

@admin.register(RestaurantLocation)
class RestaurantLocationAdmin(admin.ModelAdmin):
    list_display = {"address", "city", "state", "zip_code"}
# Register your models here.
admin.site.register(Item,ItemAdmin,Menu)
admin.site.register(RestaurantLocation)