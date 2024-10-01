from django.contrib import admin

# Register your models here.

from .models import School, EntranceExit, RoadwayFacilityNear, RoadwayFacilityFar, FinalizationForm

# admin.site.register(School)

@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('school_name','school_type','ward')
    search_fields = ('school_name','school_type')
    list_filter = ('school_name',)


admin.site.register(EntranceExit)
admin.site.register(RoadwayFacilityNear)
admin.site.register(RoadwayFacilityFar)
admin.site.register(FinalizationForm)
