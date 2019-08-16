from django.contrib import admin

from .models import Apartment, ApartmentUnit, House


@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display = ['owner', 'title', 'rent_per_month','timestamp']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(ApartmentUnit)