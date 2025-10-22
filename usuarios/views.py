from django.shortcuts import render, redirect, get_object_or_404
from usuarios.facade import UsuarioFacade

# Instanciamos la fachada
facade = UsuarioFacade()

def listar_usuarios(request):
    usuarios = facade.listar_usuarios()
    return render(request, "usuarios/listar.html", {"usuarios": usuarios})

def crear_usuario(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        rol = request.POST.get("rol")
        facade.crear_usuario(username, email, password, rol)
        return redirect("listar_usuarios")
    return render(request, "usuarios/crear.html")

def editar_usuario(request, id):
    usuario = get_object_or_404(facade.listar_usuarios(), id=id)
    if request.method == "POST":
        datos = {
            "username": request.POST.get("username"),
            "email": request.POST.get("email"),
            "rol": request.POST.get("rol"),
        }
        facade.actualizar_usuario(id, **datos)
        return redirect("listar_usuarios")
    return render(request, "usuarios/editar.html", {"usuario": usuario})

def eliminar_usuario(request, id):
    facade.eliminar_usuario(id)
    return redirect("listar_usuarios")


