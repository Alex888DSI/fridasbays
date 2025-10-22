from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    ROLES = (
        ("admin", "Administrador"),
        ("cliente", "Cliente"),
        ("empleado", "Empleado"),
    )

    rol = models.CharField(max_length=20, choices=ROLES, default="cliente")
    telefono = models.CharField(max_length=20, blank=True, null=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.username} ({self.email})"

    def activar(self):
        self.activo = True
        self.save()

    def desactivar(self):
        self.activo = False
        self.save()
