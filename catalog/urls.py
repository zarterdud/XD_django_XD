from django.urls import path
from . import views

urlpatterns = [
    path('catalog/', views.item_list),
    path('catalog/<int:pk>', views.item_detail),
]
