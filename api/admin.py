from django.contrib import admin

# Register your models here.

from .models import School, EntranceExit, RoadwayFacilityNear, RoadwayFacilityFar, FinalizationForm

admin.site.register(School)
admin.site.register(EntranceExit)
admin.site.register(RoadwayFacilityNear)
admin.site.register(RoadwayFacilityFar)
admin.site.register(FinalizationForm)
