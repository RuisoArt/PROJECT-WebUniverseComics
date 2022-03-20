from django.shortcuts import render, redirect

from my_app.models import Universe


##--------------- Mostrar Home ------------------------------------
def home(request):
    return render(request, 'universes\\home.html')


## -------------- Mostrar lista de Universos -----------------------
def list_universes(request):
    list = Universe.objects.all()

    return render(request, 'universes\\universe.html', {'universes': list})


##--------------mostrar pagina de universo------------------------------------

def marvel_comics(request):
    pagina = Universe.objects.filter(id=1)
    return render(request, 'universes\\marvel.html', {'universes': pagina})


def dc_comics(request):
    pagina = Universe.objects.filter(id=2)
    return render(request, 'universes\\dccomics.html', {'universes': pagina})


def image_comics(request):
    pagina = Universe.objects.filter(id=3)
    return render(request, 'universes\\Imagecomics.html', {'universes': pagina})


def shonen_jump(request):
    pagina = Universe.objects.filter(id=4)
    return render(request, 'universes\\ShonenJump.html', {'universes': pagina})


##  ---------------------------- capturar universo que se quiere mostrar ---------------------------------
"""
def capture_universe(request, id):
    one_universe_show = Universe.objects.get(id=id)
    return render(request, 'universes\\espec_universe.html', {'universe': one_universe_show})
"""

##  ---------------------------- mostrar universo que se dijo que se mostrara ----------------------------
"""
def mostrar_universe(request, id):
    _opinion = request.POST["opinion"]
    one_universe_show = Universe.objects.get(id=id)

    universe_show = Universe.objects.filter(id=one_universe_show.id).update(opinion=_opinion)

    one_universe_show.refresh_from_db()

    return redirect('list_universe')
"""
