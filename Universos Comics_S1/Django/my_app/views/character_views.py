from django.shortcuts import render, redirect

from my_app.models import Characters


## --------------- Mostrar lista de Personajes ------------------------
def list_characters(request):
    list = Characters.objects.all()
    return render(request, 'characters\\index.html', {'characters': list})


def list_marvel(request):
    list = Characters.objects.filter(universe_id=1)
    return render(request, 'characters\\index.html', {'characters': list})


def list_dc(request):
    list = Characters.objects.filter(universe_id=2)
    return render(request, 'characters\\index.html', {'characters': list})


def list_image(request):
    list = Characters.objects.filter(universe_id=3)
    return render(request, 'characters\\index.html', {'characters': list})


def list_shonen(request):
    list = Characters.objects.filter(universe_id=4)
    return render(request, 'characters\\index.html', {'characters': list})


## --------------------- Guardar nuevo personaje ------------------------------
def form_save(request):
    return render(request, 'characters\\form_save.html')


def save(request):
    _universe_id = request.POST["universe_id"]
    _name = request.POST["name"]
    _description = request.POST["description"]
    _imagen = request.POST["imagen"]

    oneCharacter = Characters.objects.create(name=_name, description=_description, imagen=_imagen, universe_id=_universe_id)
    return redirect('characters')


##--------- borrar un personaje ---------------------------------------------------------------------------------------------------
def delete_character(request, id):
    one_character = Characters.objects.get(id=id)
    one_character.delete()
    return redirect('characters')


## -------- captura el id que se esta mostranto para ir luego al formulario de edicion con esta informacion ------------------------
def capture_character(request, id):
    one_character_edit = Characters.objects.get(id=id)
    return render(request, 'characters\\form_edit.html', {'character': one_character_edit})


## ---------- esta funcion recibe los datos del formulario de edicion y los sube , luego refresca dirigiendo a la pagina general----------
def edit_character(request, id):
    _description = request.POST["description.es"]
    _imagen = request.POST["imagen.es"]
    one_character_edit = Characters.objects.get(id=id)

    character_update = Characters.objects.filter(id=one_character_edit.id).update(description=_description, imagen=_imagen)
    one_character_edit.refresh_from_db()  ##refresca la base de datos
    return redirect('characters')


#--------------------LOGIN-------------------------------------------
def login(request):
    return render(request, 'characters\\login.html')