from django.urls import path,include
from user_app import views

app_name='user_app'


urlpatterns = [
    path('',views.index, name='index'),
    path('registration',views.registration,name='registration'),
    path('user_login',views.user_login,name='user_login'),
    path('user_logout',views.user_logout,name='user_logout'),
    path('special_page',views.special_page,name='special_page')
]
