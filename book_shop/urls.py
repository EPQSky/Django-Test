from django.urls import path

from . import views

app_name = 'bookshop'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:role_id>/', views.detail, name='detail'),
]
