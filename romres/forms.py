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
    if self.cleaned_data.get('start_time') < timezone.now() or self.cleaned_data.get('start_time') > self.cleaned_data.get('end_time'):
      self.errors['time'] = 'asdasdadsasd'
      return False
    return True

  class Meta:
    model = Reservation
    fields = ('start_time', 'end_time', 'room', 'email', 'first_name', 'last_name', 'purpose')