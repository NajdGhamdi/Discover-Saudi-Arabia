from unicodedata import name
from destination import views
from django.urls import path
from django.urls.conf import include


app_name='destination'


urlpatterns = [
    
    path('',views.destination_list_view,name="destination_list_view"),
    path('<str:slug>',views.destination_detail_view,name="destination_detail_view"),
    path('sites/<str:slug>',views.site_detail_view,name="site_detail_view"),
    path('events/<str:slug>',views.event_detail_view,name="event_detail_view"),
    path('deletecomment/<int:id>',views.delete_comment_view,name="delete_comment_view"),
   

 ]