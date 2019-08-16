from django.urls import path

from .views import visitor as visitor_views, apartment

app_name = 'properties'

urlpatterns = [
    path('houses/', visitor_views.HouseListView.as_view(), name='house_list'),
    path('apartments/', visitor_views.ApartmentList.as_view(), name='apartment_list'),
    path('apartment-units/', apartment.ApartmentUnitListView.as_view(), name='unit_list'),
    path('<slug:slug>/', visitor_views.HouseDetailView.as_view(), name='house_detail'),
    path('apartments/<slug:slug>/', visitor_views.ApartmentDetailView.as_view(), name='apartment_detail'),  
    path('apartments/unit/<slug:slug>/', visitor_views.ApartmentUnitDetailView.as_view(), name='unit_detail'),
]
