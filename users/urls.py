from django.urls import path
from . import views



urlpatterns = [
    path('register/', views.user_register, name='user-register'),
    path('login/', views.user_login, name='login'),
    path('detai/<int:user_id>/', views.detail, name='detail'),
    path('update/<int:user_id>/', views.update, name='update'),
    path('delete/<int:user_id>/', views.delete, name='delete'),
    path('create/', views.create, name='create'),
    path('', views.users , name="Home"),
    # path('hello/', views.say_hello),

]

