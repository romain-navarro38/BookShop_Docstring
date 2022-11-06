from django.contrib import admin

from deal.models import Cart, Order, Wish


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'create_date', )
    search_fields = ('user', )
    list_filter = ('create_date', )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('book', 'user', 'quantity', 'ordered', 'ordered_date', )
    search_fields = ('book', 'user', )
    list_filter = ('ordered', 'ordered_date', )


@admin.register(Wish)
class WishAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'add_date', )
    search_fields = ('user', 'book', )
    list_filter = ('add_date', )
