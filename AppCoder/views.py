from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.forms import *
from AppCoder.models import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.


def registro(request):

    if request.method == 'POST':   

        form = FormRegistro(request.POST)   

        if form.is_valid():

            user=form.cleaned_data['username']
            form.save()
            
            return render(request, "AppCoder/inicio.html", {'mensaje':"Usuario Creado"})
    
    else:

        form = FormRegistro()   
    
    return render(request, "AppCoder/registro.html", {'form':form})




def login_request(request):

    if request.method == 'POST': 

        form = AuthenticationForm(request, data = request.POST) 

        if form.is_valid():
            
            usuario=form.cleaned_data.get('username')   
            contra=form.cleaned_data.get('password')    

            user=authenticate(username=usuario, password=contra) 

            if user:    

                login(request, user)   

                return render(request, "AppCoder/inicio.html", {'mensaje':f"Bienvenido {user}"}) 

        else:   
    
            return render(request, "AppCoder/inicio.html", {'mensaje':" Datos incorrectos"})

    else:
            
        form = AuthenticationForm() 

    return render(request, "AppCoder/login.html", {'form':form})


def editarUsuario(request):

    usuario = request.user 

    if request.method == "POST":    

        form = FormRegistro(request.POST) 

        if form.is_valid():

            informacion = form.cleaned_data   
            
            usuario.username = informacion['username']
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password1']
            
            usuario.save()

            return render(request, "AppCoder/inicio.html")

    else:

        form= FormRegistro(initial={'username':usuario.username, 'email':usuario.email})

    return render(request, "AppCoder/editarUsuario.html",{'form':form, 'usuario':usuario.username})


def sobremi(request):
    return render(request, 'AppCoder/sobremi.html')


def inicio(request):


    return render(request, 'AppCoder/inicio.html')

def busquedapaleta(request):

    return render(request, 'AppCoder/busquedapaleta.html')

@login_required
def buscarpaleta(request):

    if request.GET['marca']:

        marca=request.GET['marca']

        form = PaletasPadel.objects.filter(marca__icontains=marca)

        return render(request,'AppCoder/buscarpaleta.html',{'form':form, 'marca':marca})
    else:

        resultado = 'no enviaste datos'
        
        return HttpResponse(resultado)

def busquedapelota(request):

    return render(request, 'AppCoder/busquedapelota.html')

@login_required
def buscarpelota(request):

    if request.GET['marca']:

        marca=request.GET['marca']

        form = Pelotas.objects.filter(marca__icontains=marca)

        return render(request,'AppCoder/buscarpelota.html',{'form':form, 'marca':marca})
    else:

        resultado = 'no enviaste datos'
        
        return HttpResponse(resultado)


def Paletas (request):

    AllPaletas= PaletasPadel.objects.all()

    contexto= {'paletas':AllPaletas}

    return render(request,'AppCoder/paletas.html',contexto)

def Pelotitas (request):

    AllPelotas= Pelotas.objects.all()

    contexto= {'pelotas':AllPelotas}

    return render(request,'AppCoder/pelotas.html',contexto)

@login_required
def AddPaletas(request):

    if request.method == 'POST':

        form=PaletasPadelForm(request.POST,request.FILES)

        if form.is_valid():

            informacion = form.cleaned_data

            nuevas = PaletasPadel(nombre=informacion['nombre'], material=informacion['material'],marca=informacion['marca'],forma=informacion['forma'],precio=informacion['precio'],imagen=informacion['imagen'])

            nuevas.save()

            return render(request, 'AppCoder/inicio.html')
    else:

        form=PaletasPadelForm()

    return render(request, 'AppCoder/AddPaletas.html', {'form':form})

@login_required
def AddPelotas(request):

    if request.method == 'POST':

        form=PelotasForm(request.POST,request.FILES)

        if form.is_valid():

            informacion = form.cleaned_data

            nuevas = Pelotas(marca=informacion['marca'],precio=informacion['precio'],imagen=informacion['imagen'])

            nuevas.save()

            return render(request, 'AppCoder/inicio.html')
    else:

        form=PelotasForm()

    return render(request, 'AppCoder/AddPelotas.html', {'form':form})


@login_required
def borrarPaletas(request, nombre):

    paletas = PaletasPadel.objects.get(nombre=nombre)
    
    paletas.delete()
    
    form = PaletasPadel.objects.all()

    return render(request, "AppCoder/inicio.html",{'resultados':form})

@login_required
def borrarPelotas(request, marca):

    pelot=Pelotas.objects.get(marca=marca)
    
    pelot.delete()
    
    form=Pelotas.objects.all()


    return render(request, "AppCoder/inicio.html",{'resultados':form})


@login_required
def editarPaletas(request, nombre):

    pale = PaletasPadel.objects.get(nombre= nombre)

    if request.method == "POST":

        form = PaletasPadelForm(request.POST,request.FILES)

        if form.is_valid():

            informacion = form.cleaned_data

            pale.nombre = informacion['nombre']
            pale.material = informacion['material']
            pale.marca = informacion['marca']
            pale.forma = informacion['forma']
            pale.precio = informacion['precio']
            pale.imagen = informacion['imagen']

            pale.save()

            return render(request, "AppCoder/inicio.html")

    else:

        form= PaletasPadelForm(initial={'nombre':pale.nombre, 'material':pale.material,'marca':pale.marca, 'forma':pale.forma, 'precio':pale.precio,'imagen':pale.imagen})

    return render(request, "AppCoder/editarpaletas.html",{'form':form, 'resultado':nombre})


@login_required
def editarPelotas(request, marca):

    pelota= Pelotas.objects.get(marca=marca)

    if request.method == "POST":

        form = PelotasForm(request.POST,request.FILES)

        if form.is_valid():

            informacion = form.cleaned_data

            pelota.marca = informacion['marca']
            pelota.precio = informacion['precio']
            pelota.imagen = informacion['imagen']

            pelota.save()

            return render(request, "AppCoder/inicio.html")

    else:

        form= PelotasForm(initial={'marca':pelota.marca,'precio':pelota.precio,'imagen':pelota.imagen})

    return render(request, "AppCoder/editarpelotas.html",{'form':form, 'resultado':marca})



@login_required
def agregarimg (request):

    if request.method == "POST":

        form = AvatarForm(request.POST,request.FILES)

        if form.is_valid():

            informacion = form.cleaned_data

            avatar= Avatar(user=request.user,imagen=informacion['imagen'])

            avatar.save()


            return render(request, "AppCoder/inicio.html")

    else:

        form = AvatarForm()

        return render(request, "AppCoder/agregarimg.html", {'form':form })



