from abc import ABC, abstractmethod
from usuarios.models import Usuario

class UsuarioFactoryBase(ABC):
    """Clase abstracta base para la creación de usuarios."""
    
    @abstractmethod
    def crear_usuario(self, username, email, password):
        pass
