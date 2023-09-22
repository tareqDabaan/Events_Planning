from . import views
from django.urls import include, path
from rest_framework import routers
from .views import *

urlpatterns = [    

    path('places/', Places_List.as_view(), name='places-list'), 
    path('place/<int:pk>', Place_Id.as_view(), name='place-idt'), 

    path('images/', Images_Home_Page.as_view(), name='Images_Home_Page'),
    
    path('contactsadd/', Contacts_Add.as_view(), name='contact'),  
    path('contactsdelete/<int:pk>', Contacts_Delete.as_view(), name='contactsdelete'),  
    path('contactslist/', Contacts_List.as_view(), name='contact'), 
    
    path('photographers/', Photographer_List.as_view(), name='photographer'),

    path('cards/<int:id>', Card_List, name = 'cards'),
    path('cards/', Cards_List.as_view(), name = 'cards'),

    path('reservations_add/', create_reservation, name='reservation_add'), 
    path('reservations_list/<int:id>', Reservation_List, name='contactsdelete'),

    path('gallery/', gallery, name = 'event'),

    path('flowers/', Decoration_List_Flowers.as_view(), name = 'flowers'),
    path('balloons/', Decoration_List_Balloons.as_view(), name = 'balloons'),
    path('stands/', Decoration_List_Stands.as_view(), name = 'stands'),
    path('tables/', Decoration_List_Tables.as_view(), name = 'tables'),
    
    path('food/', Food_Packages.as_view(), name = 'food'),
    path('graduation_birthday/', Graduation_Birthday_Package.as_view(), name = 'food'),
    
    path('event/', Event.as_view(), name = 'event'),


]