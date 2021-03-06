from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='my_racehub'),
    path('order_history/<order_number>', views.order_history, name='order_history'),
    path('add_racehub_friend/', views.add_racehub_friend, name='add_racehub_friend'),
    path('add_family_and_friends/', views.add_nonracehubfriend, name='add_nonracehubfriend'),
    path('add_athlete_profile/', views.add_athlete_profile, name='add_athlete_profile'),
    path('edit_athlete_profile/<int:athleteprofile_id>/', views.edit_athlete_profile, name='edit_athlete_profile'),
    path('organiser_dashboard/', views.organiser_dashboard, name='organiser_dashboard'),
    path('delete_racehub_friend/<int:racehubfriend_id>/', views.delete_racehub_friend, name='delete_racehub_friend'),
    path('delete_nonracehub_friend/<int:nonracehubfriend_id>/', views.delete_nonracehub_friend, name='delete_nonracehub_friend'),  
    
]