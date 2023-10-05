from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.single_post_page),     #pk 값을 받아 함수에 넘김
    # path('', views.index),
    path('', views.PostList.as_view()),
]