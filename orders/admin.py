from django.contrib import admin

# Register your models here.
@admin.register(order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'status', 'total_price', 'created_at')
    list_filter = ('status', 'created_at')
    search_filter = ('customer_username', 'customer_email')
    date_hierachy = 'created_at'
    ordering = ('-created_at')

    filter_horizontal = ('items',)