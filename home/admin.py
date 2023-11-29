from django.contrib import admin
from django.contrib import admin
from event.models import RageRoomSession, Booking 
from user1.models import UserProfile

# Register your models here.


class RageRoomSessionAdmin(admin.ModelAdmin):
    list_display = ('title', 'facilitator', 'date', 'start_time', 'end_time', 'capacity')
    search_fields = ('title', 'facilitator__user__username')
    list_filter = ('date', 'facilitator')


class BookingAdmin(admin.ModelAdmin):
    list_display = ('session', 'participant', 'booking_time', 'approved')
    search_fields = ('session__title', 'participant__user__username')
    list_filter = ('session', 'approved')


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'badge_number', 'phone_number', 'age')
    search_fields = ('user__username', 'badge_number')
    list_filter = ('role',)

admin.site.register(RageRoomSession, RageRoomSessionAdmin)
admin.site.register(Booking, BookingAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
