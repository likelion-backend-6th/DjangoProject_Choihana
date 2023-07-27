from django.urls import path
from blog import views
app_name ='blog'
urlpatterns = [
    path('',views.PostLV.as_view(), name = 'list'),
    path('<int:pk>/',views.post_detail ,name = 'detail'),
    path('<int:pk>/share/',views.post_share, name ='share'),
    path('<int:pk>/comment/',views.comment, name ='comment')
]