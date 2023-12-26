from django.contrib import admin
from .models import *
from django.utils.text import slugify
# Register your models here.


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ('preview', 'name', 'description','slug')
    prepopulated_fields = {"slug": ("name",)}



@admin.register(Locations)
class AdminLocations(admin.ModelAdmin):
    list_display = ('name', 'slug', 'region')
    prepopulated_fields = {"slug": ("name",)}


@admin.register(City)
class AdminCity(admin.ModelAdmin):
    list_display = ('name', 'slug', 'region', 'location')
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Village)
class AdminVillage(admin.ModelAdmin):
    list_display = ('name', 'city', 'area')

    def area(self, obj):
        if obj.city:
            return obj.city.region
        else:
            return "--------"


@admin.register(SubCategory)
class AdminSubCategory(admin.ModelAdmin):
    list_display = ('name', 'slug',)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Products)
class AdminProducts(admin.ModelAdmin):
    list_display = ('name', 'slug','price')
    prepopulated_fields = {"slug": ("name",)}

@admin.register(YandexMetrica)
class AdminYandexMetrica(admin.ModelAdmin):
    list_display = ('counter_id',)
    search_fields = ('counter_id',)