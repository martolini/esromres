from django.contrib import admin
from .models import Room, Reservation

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
  list_display = ('id', 'size')

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
  list_display = ('room', 'email', 'start_time', 'end_time')
