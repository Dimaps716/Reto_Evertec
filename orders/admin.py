from django.contrib import admin


from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
	raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
	list_display = ['costumer_name','costumer_email','costumer_mobile','status',]
	list_filter = ['paid', 'created_at', 'updated_at']
	inlines = [OrderItemInline]


admin.site.register(Order, OrderAdmin)

