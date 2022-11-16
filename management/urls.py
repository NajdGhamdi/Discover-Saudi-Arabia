from unicodedata import name
from management import views
from django.urls import path

from django.urls.conf import include

"""the app_name variable provided for {% url 'namespace-for-url-ofproject:the nameofviewinpath' and relate it with id%}"""
app_name='management'



urlpatterns = [
    ########Destination path##########
    path('destinatons-list',views.destlist_view,name="destlist_view"),
    path('show-destinaton/<str:slug>',views.showdest_view,name="showdest_view"),
    path('update-destinaton/<str:slug>',views.updatedest_view,name="updatedest_view"),
    path('create-destinaton',views.createdest_view,name="createdest_view"),
    path('delete-destinaton/<str:slug>',views.deletedest_view,name="deletedest_view"),

    ########Site path##########
    path('sites-list',views.sitelist_view,name="sitelist_view"),
    path('show-site/<str:slug>',views.showsite_view,name="showsite_view"),
    path('update-site/<str:slug>',views.updatesite_view,name="updatesite_view"),
    path('create-site',views.createsite_view,name="createsite_view"),
    path('delete-site/<str:slug>',views.deletesite_view,name="deletesite_view"),

    ########Event path ########
    path('events-list',views.eventlist_view,name="eventlist_view"),
    path('show-event/<str:slug>',views.showevent_view,name="showevent_view"),
    path('update-event/<str:slug>',views.updateevent_view,name="updateevent_view"),
    path('create-event',views.createevent_view,name="createevent_view"),
    path('delete-event/<str:slug>',views.deleteevent_view,name="deleteevent_view"),

]