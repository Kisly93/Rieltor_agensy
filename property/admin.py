from django.contrib import admin

from .models import Flat, Complaint, Owner


class RelationInInline(admin.TabularInline):
    model = Owner.apartments.through
    raw_id_fields = ('owner',)

@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'address']
    readonly_fields = ['created_at']
    list_display = ('address', 'price', 'new_building', 'construction_year')
    list_editable = ['new_building']
    list_filter = ('new_building', 'rooms_number', 'has_balcony')
    raw_id_fields = ('likes',)
    inlines = [RelationInInline]

@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('apartment',)

@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    search_fields = ['name']
    raw_id_fields = ('apartments',)
    list_display = ('name',)



