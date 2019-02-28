from django.urls import path
from .views import Login, Logout, Signup, home, event_list, event_create, event_detail, event_update,profile
from events import views
from django.conf import settings
from django.conf.urls.static import static
from API.views import (
        EventList,
        EventDetail,
        EventCreate,
        EventUpdate,
        EventDelete,
 )

urlpatterns = [
	path('', home, name='home'),
    path('signup/', Signup.as_view(), name='signup'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),


    path('list/', views.event_list, name='event-list'),
    path('create/', views.event_create, name='event-create'),
    path('detail/<int:event_id>/', views.event_detail, name='event-detail'),
    path('update/<int:event_id>/', views.event_update, name='event-update'),
    path('delete/<int:event_id>/', views.event_delete, name='event-delete'),

    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('booking/<int:event_id>/', views.booking, name='booking'),

    path('recently/', views.recently_events, name='recently-event'),
    path('profile/', views.profile, name='profile'),


    #API URLs
    path('api/',EventList.as_view(), name='api-list'),
    path('create/add/',EventCreate.as_view(), name='api-create'),
    path('api/update/<int:event_id>/',EventUpdate.as_view(), name='api-update'),
    path('api/detail/<int:event_id>/',EventDetail.as_view(), name='api-detail'),
    path('api/delete/<int:event_id>/',EventDelete.as_view(), name='api-delete'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
