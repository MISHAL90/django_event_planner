from django import forms
from .models import Event ,Booking
from django.contrib.auth.models import User
 
class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        exclude = ['organizer',]
        

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['number_of_ticket',]


class UserSignup(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email' ,'password']

        widgets={
        'password': forms.PasswordInput(),
        }



class UserLogin(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput())

