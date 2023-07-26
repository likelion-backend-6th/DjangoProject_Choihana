from django.urls import path
from blog import views
app_name ='blog'
urlpatterns = [
    path('',views.PostLV.as_view(), name = 'list'),
    path('<int:pk>/',views.PostDV.as_view(),name = 'detail')
]