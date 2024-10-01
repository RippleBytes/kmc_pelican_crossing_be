from django.urls import path
import api.views as views

urlpatterns = [
    path('roadway-near/<int:school_id>', views.roadway_near_school_submission, name='roadway_form_submission'),
    path('roadway-far/<int:school_id>', views.roadway_far_from_school_submission, name='roadway_far_from_school_submission'),

    path('', views.school_form_view, name='school_form'),
    path('finalize/<int:school_id>', views.finalize_form_view, name='finalize'),
    path('complete/<int:school_id>', views.complete, name='complete'),
]
