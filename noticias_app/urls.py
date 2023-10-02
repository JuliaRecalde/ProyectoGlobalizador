from django.urls import path
from . import views

urlpatterns = [
    #path('obtener_noticias/', views.obtener_noticias, name='obtener_noticias'),
    
    #path(''),
    #path('noticia/<int:noticia_id>/', views.detalle_noticia, name='detalle_noticia'),

    path('', views.obtener_noticias, name='obtener_noticias'),
    
]