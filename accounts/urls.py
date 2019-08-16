'''
All the URL configs here are for the CMS redirects. These paths are only accessable for
authenticated users.
'''

from django.urls import path
from django.views.generic import TemplateView

from .views import AgentSubmitDocumentView, MyDocumentListView, verify_agent, confirm_verification
from blog.views import ArticleCreateView, ArticleDeleteView, ArticleUpdateView, MyArticleListView
from properties.views.house import (HouseCreateView, MyHouseListView, HouseUpdateView,
                                    HouseDeleteView)
from properties.views.apartment import (ApartmentCreateView, ApartmentUpdateView, ApartmentDeleteView, ApartmentUnitCreateView, ApartmentUnitDeleteView, 
                                        ApartmentUnitUpdateView, MyApartmentListView, MyApartmentUnitListView, ApartmentUnitDeleteView)

app_name = 'account'

urlpatterns = [
    path('', TemplateView.as_view(template_name='overview.html'), name='dashboard'),

    # apartments
    path('apartments/', MyApartmentListView.as_view(), name='apartment_list'),
    path('apartments/create/', ApartmentCreateView.as_view(), name='create_apartment'),
    path('apartments/<slug:slug>/update/', ApartmentUpdateView.as_view(), name='update_apartment'),
    path('apartments/<slug:slug>/delete/', ApartmentDeleteView.as_view(), name='delete_apartment'),
    # house 
    path('houses/', MyHouseListView.as_view(), name='house_list'),
    path('houses/add-house/', HouseCreateView.as_view(), name='create_house'),
    path('houses/<slug:slug>/update/', HouseUpdateView.as_view(), name='update_house'),
    path('houses/<slug:slug>/delete/', HouseDeleteView.as_view(), name='delete_house'),
    # apartment units
    path('units/', MyApartmentUnitListView.as_view(), name='apartmentunit_list'),
    path('units/add-unit/', ApartmentUnitCreateView.as_view(), name='create_unit'),
    path('units/<slug:slug>/update/', ApartmentUnitUpdateView.as_view(), name='update_unit'),
    path('units/<slug:slug>/delete/', ApartmentUnitDeleteView.as_view(), name='delete_unit'),
    # document
    path('documents/', MyDocumentListView.as_view(), name='document_list'),
    path('documents/<slug:slug>/verify/', verify_agent, name='verify_agent'),
    path('confirm-verification/<slug:slug>/', confirm_verification, name='confirm'),
    path('submit-document/', AgentSubmitDocumentView.as_view(), name='submit_document'),
    
    # blog articles
    
    path('articles/', MyArticleListView.as_view(), name='article_list'),
    path('articles/write-article/', ArticleCreateView.as_view(), name='write_article'),
    path('articles/<slug:slug>/update/', ArticleUpdateView.as_view(), name='update_article'),
    path('articles/<slug:slug>/delete/', ArticleDeleteView.as_view(), name='delete_article'),
]
