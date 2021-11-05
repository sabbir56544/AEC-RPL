from django.urls import path
from .views import home, category, category_detail, autosuggest, serach_courses


urlpatterns = [
    path('', home, name='home'),
    path('category/<str:cat_name>', category, name='category'),
    path('detail/<int:pk>', category_detail, name='category_detail'),
    path('autosuggest/', autosuggest, name='autosuggest'),
    path('search', serach_courses, name='search'),
]