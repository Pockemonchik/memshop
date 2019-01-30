from django.contrib import admin
from shop.models import mem,Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category, CategoryAdmin)

admin.site.register(mem)
# Register your models here.
