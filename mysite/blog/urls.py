from django.urls import path
from blog import views
app_name ='blog'
urlpatterns = [
    path('',views.PostLV.as_view(), name = 'index'),
]