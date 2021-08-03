from django.contrib import admin
from apps.orders.models import Order

# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'status', 'car', )
    autocomplete_fields = ('car', )


admin.site.register(Order, OrderAdmin)