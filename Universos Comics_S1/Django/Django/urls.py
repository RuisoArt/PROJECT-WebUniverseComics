from django.contrib import admin
from django.urls import path

from my_app.views import character_views
from my_app.views import universe_views
from my_app.views import login_views

urlpatterns = [

    path('admin/', admin.site.urls),

    path('home/', universe_views.home, name='home'),

    path('list/', character_views.list_characters, name='characters'),
    path('list_marvel/', character_views.list_marvel, name='characters_marvel'),
    path('list_dc/', character_views.list_dc, name='characters_dc'),
    path('list_image/', character_views.list_image, name='characters_image'),
    path('list_shonen/', character_views.list_shonen, name='characters_shonen'),

    path('marvel/', universe_views.marvel_comics, name='marvel_comics'),
    path('dc/', universe_views.dc_comics, name='dc_comics'),
    path('image/', universe_views.image_comics, name='image_comics'),
    path('shonen/', universe_views.shonen_jump, name='shonen_jump'),

    path('universe_list/' , universe_views.list_universes, name='list_universe'),
    #path('show_universe/<int:id>', universe_views.mostrar_universe, name='show_universe'),
    #path('capture_universe/<int:id>', universe_views.capture_universe, name='capture_universe'),

    path('list/form_save/', character_views.form_save, name='form_character'),
    path('list/save/', character_views.save, name='save_character'),

    path('delete/<int:id>', character_views.delete_character, name='delete_character'),
    path('edit_character/<int:id>', character_views.edit_character, name='edit_character'),
    path('capture_character/<int:id>', character_views.capture_character, name='capture'),

    path('login/', character_views.login, name='login'),
    #path('logout/', login_views.logout_system, name='logout'),



]
