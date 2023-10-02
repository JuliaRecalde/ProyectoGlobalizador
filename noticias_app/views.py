
# Create your views here.
import requests
from django.shortcuts import render
from .models import Noticia
from django.conf import settings

def obtener_noticias(request):
    api_key = settings.NEWSAPI_KEY
    base_url = 'https://newsapi.org/v2/top-headlines'
    parametros = {
        'country': 'PY',
        'apiKey': api_key
    }
    
    response = requests.get(base_url, params=parametros)
    response = requests.get(base_url, params=parametros)
    print(response.json()) 
    if response.status_code == 200:
        noticias_json = response.json()['articles']
        
        # Guardar noticias en la base de datos
        for noticia_data in noticias_json:
            noticia = Noticia(
                titulo=noticia_data['title'],
                descripcion=noticia_data['description'],
                enlace=noticia_data['url'],
                fecha_publicacion=noticia_data['publishedAt'],
                palabra_clave='PARAGUAY'
            )
            noticia.save()
        
        noticias = Noticia.objects.all()
        return render(request, 'noticias.html', {'noticias': noticias})
    else:
        return render(request, 'error.html')