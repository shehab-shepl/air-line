from django.contrib import admin

from .models import Airport, Flight, Passenger

# Register your models here.

class FlightAdmin(admin.ModelAdmin):
    list_display = ("__str__", "duration")



class PassengerAdmin(admin.ModelAdmin):

# special way of manipulating many to many relationships inside
    filter_horizontal = ("flights",)
    

admin.site.register(Airport)
admin.site.register(Flight, FlightAdmin)
admin.site.register(Passenger, PassengerAdmin)
