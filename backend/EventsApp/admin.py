from django.contrib import admin
from .models import *


class FinalReservationAdmin(admin.ModelAdmin):
    list_display = ('customerName','place_date')
    list_filter = ('date','place',)
    def place_date(self, obj):
        return "{} , {}".format(obj.place, obj.date)


class PlaceAdmin(admin.ModelAdmin):
    list_display =('name','cost','location','combine_location_and_cost')
    list_filter = ('name','cost',) # This will allows a filter button 
    
    fieldsets =((
        None,
        {
            'fields':(
                'name',
                'location',
                'crew',
                'eventID',
                'capacity',
                'cost',
                'image',
                'period',
                'rate',
            )
        }),
    )
    def combine_location_and_cost(self, obj):
        return "{} , {}".format(obj.location, obj.cost)

        
admin.site.register(Place, PlaceAdmin)
admin.site.register(HomePageGallery)
admin.site.register(Card)
admin.site.register(Decoration)
admin.site.register(Gallery)
admin.site.register(Event)
admin.site.register(Food)
admin.site.register(Photographer)
admin.site.register(ContactUs)
admin.site.register(FinalReservation, FinalReservationAdmin)
