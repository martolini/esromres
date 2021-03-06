# -*- coding: utf-8 -*-

from django.shortcuts import render
from .models import Room, Reservation
from django.db.models import Prefetch
from django.utils import timezone
from .forms import ReservationForm
from datetime import datetime
from django.contrib import messages

def index_view(request):
  form = ReservationForm(initial={'email': '', 'first_name': '', 'last_name': '', 'purpose': ''})
  if request.POST:
    form = ReservationForm(request.POST)
    if form.is_valid():
      reservation = form.save()
      messages.success(request, "Du har nå reservert rom {} fra {} til {}".format(
        reservation.room_id, reservation.start_time.strftime('%d %B %H:00'), reservation.end_time.strftime('%H:00')))
    else:
      for k, v in form.errors.items():
        messages.warning(request, v)
  if request.GET.get('browseday', False):
    date = timezone.get_current_timezone().localize(datetime.strptime(request.GET.get('browseday'), '%d/%m/%Y'))
  else:
    date = timezone.localtime(timezone.now())
  raw_rooms = Room.objects.all().prefetch_related(Prefetch('reservations', queryset=Reservation.objects.for_day(date).order_by('start_time'), to_attr='today'))
  intervals = range(7, 22)
  rooms = []
  for room in raw_rooms:
    room_intervals = {}
    for reservation in room.today:
      hours = reservation.get_booked_hours()
      for hour in hours:
        room_intervals[hour] = reservation
    keys = room_intervals.keys()
    booked_hours = [False if x not in keys else room_intervals[x] for x in intervals]
    runner = booked_hours[0]
    hours = 1
    output = []
    for elem in booked_hours[1:]:
      if elem != runner:
        output.append({'length': hours, 'booked': runner})
        hours = 0
        runner = elem
      hours += 1
    output.append({'length': hours, 'booked': runner})
    rooms.append({
      'id': room.id,
      'size': room.size,
      'intervals': output
    })


  return render(request, 'romres/index.html', {
    'rooms': rooms, 'intervals': intervals, 'date': date, 'form': form
  })
