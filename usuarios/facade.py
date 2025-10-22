from usuarios.factory.usuario_factory import ClienteFactory, AdminFactory, EmpleadoFactory
from usuarios.services.usuario_service import UsuarioService

class UsuarioFacade:
    """
    Fachada que centraliza el acceso a las operaciones de usuarios.
    Simplifica la interacción entre la vista y las capas internas.
    """

    def __init__(self):
        self.service = UsuarioService()
        self.factories = {
            "cliente": ClienteFactory(),
            "admin": AdminFactory(),
            "empleado": EmpleadoFactory(),
        }

    def crear_usuario(self, tipo, username, email, password):
        factory = self.factories.get(tipo)
        if not factory:
            raise ValueError(f"Tipo de usuario '{tipo}' no válido.")
        return factory.crear_usuario(username, email, password)

    def actualizar_usuario(self, id_usuario, **datos):
        return self.service.actualizar_usuario(id_usuario, **datos)

    def eliminar_usuario(self, id_usuario):
        return self.service.eliminar_usuario(id_usuario)

    def listar_usuarios(self):
        return self.service.listar_usuarios()
