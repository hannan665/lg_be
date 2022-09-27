from django.contrib import admin

from main.models import Services, SubProduct, Product, ColorTone, Industry, Logo, TypeAndPreferences


# Register your models here.

class ServicesInline(admin.StackedInline):
    model = Services


@admin.register(SubProduct)
class SubProductAdmin(admin.ModelAdmin):
    # list_display = ["course","name","created_by"]
    inlines = [ServicesInline]
    list_display = ["title", "image"]

@admin.register(Logo)
class LogoAdmin(admin.ModelAdmin):
    list_display = ['email', "business_name", "user_name"]
    # inlines = [ServicesInline]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['price', "title", "image"]
# admin.site.register(Product)

# admin.site.register(Product)
admin.site.register(ColorTone)
admin.site.register(Industry)
admin.site.register(TypeAndPreferences)
