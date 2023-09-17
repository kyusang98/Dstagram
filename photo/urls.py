from django.urls import path
from django.views.generic.detail import DetailView
from .views import *
from .models import Photo

app_name = 'photo'

urlpatterns = [
    #함수형뷰
    path('',photo_list,name='photo_list'),
    #클래스형뷰
    path('detail/<int:pk>/',DetailView.as_view(model=Photo,template_name='photo/detail.html'), name='photo_detail'),
    path('upload/', PhotoUploadView.as_view(), name='photo_upload'),
    path('delete/<int:pk>/',PhotoDeleteView.as_view(),name='photo_delete'),
    path('update/<int:pk>/',PhotoUploadView.as_view(), name='photo_update'),
]
