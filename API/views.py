from rest_framework.generics import (
	ListAPIView,
	RetrieveAPIView,
	RetrieveUpdateAPIView,
	RetrieveDestroyAPIView,
	CreateAPIView
)

from events.models import Event

from .serializers import (
		EventListSerializer,
		EventDetailSerializer,
		EventCreateUpdateSerializer,
)	

from rest_framework.permissions import AllowAny, IsAuthenticated

from .permissions import Event_Permissions

class EventList (ListAPIView):
	queryset = Event.objects.all()
	serializer_class = EventListSerializer
	permissions_classes = [ AllowAny ]

class EventDetail (RetrieveAPIView):
	queryset = Event.objects.all()
	serializer_class = EventDetailSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'event_id'
	permission_classes = [ AllowAny ]

class EventCreate (CreateAPIView):
	serializer_class = EventCreateUpdateSerializer
 
	def perform_create(self, serializer):
		serializer.save(organizer=self.request.user)
 

class EventUpdate (RetrieveUpdateAPIView):
	queryset = Event.objects.all()
	serializer_class = EventCreateUpdateSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'event_id'
	permission_classes = [ Event_Permissions ]


class EventDelete (RetrieveDestroyAPIView):
	queryset = Event.objects.all()
	lookup_field = 'id'
	lookup_url_kwarg = 'event_id'
	permission_classes = [ IsAuthenticated ]
