from rest_framework import serializers
from .models import *


# A serializer To render Place Data to the FrontEnd
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

        
class PlaceSerializer(serializers.ModelSerializer):
    eventname=EventSerializer(many=True,read_only=True)
    class Meta:
        model = Place
        fields = '__all__'
       

class HomePageGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = HomePageGallery
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = '__all__'


class PhotographerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photographer
        fields = '__all__'


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'

class GraduationBirthdaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ['id','eventID','packageName','img','cost','Drinks','Entrees','Desserts']

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'    


class DecorationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Decoration
        fields = ['id','category','imgURL','cost']


class FinalReservationSerializer(serializers.ModelSerializer):

    class Meta:
        model = FinalReservation
        fields = '__all__'


class OnlyDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinalReservation
        fields = ['date']

class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = '__all__'