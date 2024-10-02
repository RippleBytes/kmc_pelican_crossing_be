from django.contrib import admin

# Register your models here.

from .models import School, EntranceExit, RoadwayFacilityNear, RoadwayFacilityFar, FinalizationForm
from import_export.admin import ExportActionModelAdmin

# admin.site.register(School)


class EntranceExitInline(admin.StackedInline):
    model = EntranceExit
    extra = 1


class RoadwayFacilityNearInline(admin.StackedInline):
    model = RoadwayFacilityNear
    extra = 1


class RoadwayFarInline(admin.StackedInline):
    model = RoadwayFacilityFar
    extra = 1


class FinalizationFormInline(admin.StackedInline):
    model = FinalizationForm
    extra = 1


@admin.register(School)
class SchoolAdmin(ExportActionModelAdmin, admin.ModelAdmin):
    list_display = ('school_name','school_type','ward')
    search_fields = ('school_name','school_type')
    list_filter = ('school_name',)
    inlines = [EntranceExitInline, RoadwayFacilityNearInline, RoadwayFarInline, FinalizationFormInline]


@admin.register(EntranceExit)
class EntranceExitAdmin(ExportActionModelAdmin, admin.ModelAdmin):
    list_display = ('school__school_name',)


@admin.register(RoadwayFacilityNear)
class RoadwayFacilityNearAdmin(ExportActionModelAdmin, admin.ModelAdmin):
    list_display = ('school__school_name',)


@admin.register(RoadwayFacilityFar)
class RoadwayFacilityFarAdmin(ExportActionModelAdmin, admin.ModelAdmin):
    list_display = ('school__school_name',)


@admin.register(FinalizationForm)
class FinalizationFormAdmin(ExportActionModelAdmin, admin.ModelAdmin):
    list_display = ('school__school_name',)
