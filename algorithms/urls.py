from django.urls import path
from . import views

# int:pk 는 정수 형태의 값을 pk라는 변수로 담아 함수로 넘기겠다는 말이다.
urlpatterns = [
    path('', views.PostList.as_view()),
    path('<int:pk>/', views.single_post_page),
]