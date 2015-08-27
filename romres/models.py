from django.db import models
from django.utils import timezone

class ReservationManager(models.Manager):
  def today(self):
    today = timezone.localtime(timezone.now())
    return self.filter(start_time__day=today.day, start_time__month=today.month)

  def for_day(self, date):
    return self.filter(start_time__day=date.day, start_time__month=date.month)

class Room(models.Model):
  id = models.SmallIntegerField(primary_key=True)
  size = models.SmallIntegerField(default=4)

  def get_booked_intervals(self):
    intervals = []
    for reservation in self.reservations.today():
      intervals.extend((range(int(timezone.localtime(reservation.start_time).hour), int(timezone.localtime(reservation.end_time).hour+.5))))
    return intervals

  def __unicode__(self):
    return '{}'.format(self.id)

class Reservation(models.Model):
  room = models.ForeignKey(Room, related_name='reservations')
  start_time = models.DateTimeField()
  end_time = models.DateTimeField()
  purpose = models.CharField(max_length=100)
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  email = models.EmailField()
  objects = ReservationManager()

  def get_booked_hours(self):
    return range(int(timezone.localtime(self.start_time).hour), int(timezone.localtime(self.end_time).hour+.5))

  def __unicode__(self):
    return '{} for {}'.format(self.room_id, self.email)