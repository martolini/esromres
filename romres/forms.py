# -*- coding: utf-8 -*-

from django import forms
from .models import Reservation
import datetime
from django.utils import timezone
from django.conf import settings

class ReservationForm(forms.ModelForm):
  start_time = forms.CharField(required=True)
  end_time = forms.CharField(required=True)

  def clean_start_time(self):
    return timezone.get_current_timezone().localize(datetime.datetime.strptime(self.data.get('start_time'), '%d %B %Y %H:%M'))

  def clean_end_time(self):
    return timezone.get_current_timezone().localize(datetime.datetime.strptime(self.data.get('end_time'), '%d %B %Y %H:%M'))

  def is_valid(self):
    valid = super(ReservationForm, self).is_valid()
    if not valid:
      return valid
    start_time = self.cleaned_data.get('start_time')
    end_time = self.cleaned_data.get('end_time')
    if start_time == end_time:
      self.errors['time'] = u'Du må booke rommet i minste en time.'
      return False
    if start_time < timezone.now():
      self.errors['time'] = u'Du kan ikke reservere tilbake i tid...?'
      return False
    elif start_time > end_time:
      self.errors['time'] = u'Du kan ikke slutte før du har startet. Komånn.'
      return False
    elif self.cleaned_data.get('room').is_booked_for_interval([start_time, end_time]):
      self.errors['time'] = u'Rommet er allerede booket.'
      return False
    return True

  class Meta:
    model = Reservation
    fields = ('start_time', 'end_time', 'room', 'email', 'first_name', 'last_name', 'purpose')