from django.contrib import admin
from .models import Item, Ingredient

class IngredientInline(admin.TabularInline):
    model = Ingredient
    fk_name = 'makes'
    fields = ('item', 'quantity')
    extra = 9

class ItemAdmin(admin.ModelAdmin):
    inlines = [
        IngredientInline,
    ]
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name', 'slug', 'batch_size')
    search_fields = ('name',)

admin.site.register(Item, ItemAdmin)