from django.urls import path
import api.views as views

urlpatterns = [
    path('roadway-near/', views.roadway_near_school_submission, name='roadway_form_submission'),
    path('roadway-far/', views.roadway_far_from_school_submission, name='roadway_far_from_school_submission'),

    path('initial/', views.school_form_view, name='school_form'),
    path('complete/', views.complete, name='complete'),
]
