from django.urls import path
from . import views

app_name = 'quantum_gan'
urlpatterns = [
    path('', views.index, name='index'),
    path('plot', views.img_plot, name="img_plot"),
]