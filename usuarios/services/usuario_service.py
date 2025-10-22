from usuarios.models import Usuario

class UsuarioService:
    """
    Capa de servicio que contiene la lógica de negocio
    para las operaciones CRUD de Usuario.
    """

    @staticmethod
    def crear_usuario(username, email, password, rol="cliente"):
        usuario = Usuario.objects.create_user(username=username, email=email, password=password, rol=rol)
        return usuario

    @staticmethod
    def actualizar_usuario(id_usuario, **datos):
        Usuario.objects.filter(id=id_usuario).update(**datos)
        return Usuario.objects.get(id=id_usuario)

    @staticmethod
    def eliminar_usuario(id_usuario):
        usuario = Usuario.objects.get(id=id_usuario)
        usuario.delete()

    @staticmethod
    def listar_usuarios():
        return Usuario.objects.all()
