from django.contrib import admin

from .models import Flat, Complaint, Owner


class RelationInInline(admin.TabularInline):
    model = Owner.owner_apartment.through
    raw_id_fields = ('owner',)


class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'address']
    readonly_fields = ['created_at']
    list_display = ('address', 'price', 'new_building', 'construction_year')
    list_editable = ['new_building']
    list_filter = ('new_building', 'rooms_number', 'has_balcony')
    raw_id_fields = ('likes',)
    inlines = [RelationInInline]


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('apartment',)


class OwnerAdmin(admin.ModelAdmin):
    search_fields = ['owner_name']
    raw_id_fields = ('owner_apartment',)
    list_display = ('owner_name',)


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Owner, OwnerAdmin)
