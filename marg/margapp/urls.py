from django.urls import path
from . import views

urlpatterns = [
    path('', views.input_form, name='input_form'),  # Show the form
    path('submit/', views.input_form, name='submit_data'),  # Handle form submission
    path('show_data/', views.show_data, name='show_data'),  # Show all stored data
]
