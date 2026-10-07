from django.shortcuts import render

# Data enviada desde la vista hacia los templates (Punto 2 de la pauta)
PELICULAS_DATA = {
    'accion': {
        'nombre_genero': 'Acción',
        'descripcion': 'Películas llenas de adrenalina, combates y persecuciones.',
        'peliculas': [
            {'nombre': 'Mad Max: Fury Road', 'edad': '+16', 'imagen': 'images/madmax.jpg'},
            {'nombre': 'John Wick', 'edad': '+18', 'imagen': 'images/johnwick.jpg'}
        ]
    },
    'comedia': {
        'nombre_genero': 'Comedia',
        'descripcion': 'Historias divertidas para reír con amigos y familia.',
        'peliculas': [
            {'nombre': 'Superbad', 'edad': '+16', 'imagen': 'images/superbad.jpg'},
            {'nombre': 'Son Como Niños', 'edad': '+13', 'imagen': 'images/soncomoninos.jpg'}
        ]
    }
}

def inicio(request):
    return render(request, 'home_matias_pena/inicio.html', {'generos': PELICULAS_DATA})

def detalle_genero(request, genero_id):
    genero_info = PELICULAS_DATA.get(genero_id)
    return render(request, 'home_matias_pena/genero.html', {'genero': genero_info})