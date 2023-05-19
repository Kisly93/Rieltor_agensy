from django.contrib import admin

from .models import Flat, Complaint, Owner


class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'address', 'owner_name']
    readonly_fields = ['created_at']
    list_display = ('address', 'price', 'new_building', 'construction_year', 'owners_phonenumber', 'owner_pure_phone')
    list_editable = ['new_building']
    list_filter = ('new_building', 'rooms_number', 'has_balcony')
    raw_id_fields = ('likes',)


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('apartment',)

class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('owner_apartment',)
    list_display = ('owner_name',)



admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Owner, OwnerAdmin)
