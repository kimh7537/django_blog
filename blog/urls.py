from django.urls import path
from . import views

urlpatterns = [
    # path('<int:pk>/', views.single_post_page),     #pk 값을 받아 함수에 넘김
    # path('', views.index),
    path('category/<str:slug>/', views.category_page),
    path('<int:pk>/', views.PostDetail.as_view()),
    path('', views.PostList.as_view()),
]