from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import User, LoginCredentials, Address

# Register your models here.
admin.site.register(User)
class UserAdmin(OSMGeoAdmin):
    list_display = ('name', 'contact_no', 'email_id', 'profile_pic', 'profile_status', 'is_special_entity')

admin.site.register(Address)
class AddressAdmin(OSMGeoAdmin):
    list_display = ('user', 'location', 'city', 'state', 'country')

admin.site.register(LoginCredentials)
class LoginCredentials(OSMGeoAdmin):
    list_display = ('user', 'user_password')

