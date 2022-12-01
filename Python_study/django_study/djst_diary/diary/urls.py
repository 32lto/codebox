from django.urls import path

from . import views

app_name = 'diary'
urlpatterns = [
    path('', views.IndexView.as_view(), name="Index"),
    path('hoge/', views.IndexView2.as_view(), name="Hoge"),
    path('foo/', views.Sugenakore.as_view(), name="Fooo"),
]