from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views import View
from .forms import UserSignup, UserLogin, EventForm, BookingForm
from .models import Event, Booking
from django.contrib import messages
from django.db.models import Q
import datetime
from django.contrib.auth.models import User

def profile(request):
    profiles = request.user
    context = {
        "profiles": profiles,
     }
    return render(request, 'profile.html', context)





def recently_events(request):
  
    recently_event = request.user.bookings.all()
    #ticket = Booking.objects.filter(name=request.user)filter(event__date__lt= datetime.date.today())

    context = {
       
        #"ticket":ticket,
        "recently_event": recently_event
    }
    return render(request, 'recently.html', context)

def dashboard_view(request):
    events = Event.objects.filter(organizer=request.user)
 

    context = {
        "events": events,
       
    }
    return render(request, 'dashboard.html', context)

#filter(post_date__date=date.today())
#.filter(date__gte=datetime.date.today()).order_by("-date" )
def event_list(request):
    events = Event.objects.filter(date__gte=datetime.date.today()).order_by("-date" )
    query = request.GET.get('Search')
    if query:
           events = events.filter(
           Q(title__icontains=query)|
           Q(description__icontains=query)|
           Q(organizer__username__icontains=query)
       ).distinct()

    context = {
        "events": events,
    }

    return render(request, 'event_list.html', context)

def event_detail(request, event_id):
    event = Event.objects.get(id=event_id)
    ticket = event.bookings.all()


    context = {
        "event": event,
        "ticket":ticket,
    }

    return render(request, 'event_detail.html', context)

def booking(request, event_id):
    event = Event.objects.get(id=event_id)
    if  (request.user.is_anonymous):
        messages.success(request, 'YOU CAN NOT  ')
        return redirect('login')

    form = BookingForm()
    if request.method == "POST":
        form = BookingForm(request.POST)
        if event.get_remain_ticket() == 0:
            print('no you can not')


        elif int(form['number_of_ticket'].value()) > event.get_remain_ticket():
            
            messages.warning(request, 'too many!')
        
        elif form.is_valid():
                booking= form.save(commit=False)
                booking.event = event
                booking.name =request.user 
                booking.save()
                messages.success(request, 'well done !')
                return redirect('dashboard')
                print(form.errors)
    context = {
    "form": form,
    "event": event,
    }
    return render(request, 'booking.html', context)


def event_create(request):
    form = EventForm()
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES or None)
        if form.is_valid():
            event= form.save(commit=False)
            event.organizer = request.user
            event.save()
            messages.success(request, "Successfully Created!")
            return redirect('event-list')
        print (form.errors)
    context = {
    "form": form,
    }
    return render(request, 'event_create.html', context)


def event_update(request, event_id):
    event = Event.objects.get(id=event_id)
    if not (request.user == event.organizer):
        messages.success(request, 'nooop you can not !')
        return redirect('event-list')
    form = EventForm(instance=event)
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES or None, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully Edited!")
            return redirect('event-list')
        print (form.errors)
    context = {
    "form": form,
    "event": event,
    }
    return render(request, 'event_update.html', context)

def event_delete(request, event_id):
     event = Event.objects.get(id=event_id)
     if not (request.user == event.organizer):
        messages.success(request, "sd!")
        return redirect('event-list')
     event.delete()
     messages.success(request, "Successfully Deleted!")
     return redirect('event-list')

def home(request):
    return render(request, 'home.html')

class Signup(View):
    form_class = UserSignup
    template_name = 'signup.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()
            messages.success(request, "You have successfully signed up.")
            login(request, user)
            return redirect("home")
        messages.warning(request, form.errors)
        return redirect("signup")


class Login(View):
    form_class = UserLogin
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            auth_user = authenticate(username=username, password=password)
            if auth_user is not None:
                login(request, auth_user)
                messages.success(request, "Welcome Back!")
                return redirect('home')
            messages.warning(request, "Wrong email/password combination. Please try again.")
            return redirect("login")
        messages.warning(request, form.errors)
        return redirect("login")


class Logout(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        messages.success(request, "You have successfully logged out.")
        return redirect("login")

