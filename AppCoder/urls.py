from django.urls import path
from AppCoder.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [

    path('inicio/',inicio, name="inicio"),
    path('paletas/', Paletas,name="paletas"),
    path('pelotas/',Pelotitas, name="pelotas"),
    path('AddPaletas/',AddPaletas, name="AddPaletas"),
    path('AddPelotas/',AddPelotas, name="AddPelotas"),
    path('editarpaletas/<nombre>',editarPaletas, name="editarpaletas"),
    path('editarpelotas/<marca>',editarPelotas, name="editarpelotas"),
    path('borrarPaletas/<nombre>',borrarPaletas, name="borrarPaletas"),
    path('borraPelotas/<marca>',borrarPelotas, name="borrarPelotas"),
    path('agregarimg/',agregarimg, name="Avatar"),
    path('busquedapaleta/', busquedapaleta,name='busquedapaleta'),
    path('buscarpaleta/',buscarpaleta, name="buscarpaleta"),
    path('busquedapelota/', busquedapelota,name='busquedapelota'),
    path('buscarpelota/',buscarpelota, name="buscarpelota"),   



    path('login/', login_request, name = 'login'),
    path('logout/', LogoutView.as_view(template_name='AppCoder/logout.html'), name='logout'),
    path('registro/', registro, name = 'registro'),
    path("editarUsuario/", editarUsuario, name="Editar Usuario"),
    path('sobremi/', sobremi, name = 'sobremi'),



]