from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Event(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    date = models.DateField()
    img = models.ImageField()
    capacity = models.IntegerField()
    location = models.TextField()
    organizer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='events')
    

    def get_absolute_url(self):
        return reverse('event-detail', kwargs={'event_id':self.id})

    def get_remain_ticket(self):
        return self.capacity - sum(self.bookings.all().values_list('number_of_ticket',flat=True))



class Booking(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    number_of_ticket = models.IntegerField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='bookings')

    