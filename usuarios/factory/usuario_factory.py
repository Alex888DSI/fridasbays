from usuarios.factory.base_factory import UsuarioFactoryBase
from usuarios.models import Usuario

class ClienteFactory(UsuarioFactoryBase):
    def crear_usuario(self, username, email, password):
        return Usuario.objects.create_user(username=username, email=email, password=password, rol="cliente")

class AdminFactory(UsuarioFactoryBase):
    def crear_usuario(self, username, email, password):
        return Usuario.objects.create_user(username=username, email=email, password=password, rol="admin")

class EmpleadoFactory(UsuarioFactoryBase):
    def crear_usuario(self, username, email, password):
        return Usuario.objects.create_user(username=username, email=email, password=password, rol="empleado")
