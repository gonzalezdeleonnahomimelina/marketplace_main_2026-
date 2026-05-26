from django.contrib import admin
from .models import User, Category, Product, Cart, CartItem

# Configuración del modelo User
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_seller', 'is_staff')
    list_filter = ('is_seller', 'is_staff')
    search_fields = ('username', 'email')

# Configuración del modelo Category
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

# Configuración del modelo Product
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'owner', 'created_at')
    list_filter = ('categories', 'created_at')
    search_fields = ('name', 'description')

# Permite ver y editar los productos del carrito directamente desde el panel del Carrito
class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 1
    # Mostramos el subtotal calculado como campo de solo lectura
    readonly_fields = ('subtotal',) 

# Configuración del modelo Cart
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'total', 'created_at') # Agregamos 'total' a la vista de lista
    inlines = [CartItemInline]

# Configuración del modelo CartItem
@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'quantity', 'subtotal') # Agregamos 'subtotal' aquí también