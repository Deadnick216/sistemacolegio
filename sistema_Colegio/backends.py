from django.contrib.auth.backends import BaseBackend
from sistema_Colegio.models import Estudiante, Docente, Nodocente

class EstudianteBackend(BaseBackend):
    def authenticate(self, request, rut=None, **kwargs):
        try:
            estudiante = Estudiante.objects.get(rut=rut)
            return estudiante
        except Estudiante.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Estudiante.objects.get(pk=user_id)
        except Estudiante.DoesNotExist:
            return None

class DocenteBackend(BaseBackend):
    def authenticate(self, request, correo=None, password=None, **kwargs):
        try:
            docente = Docente.objects.get(correo=correo)
            if docente.check_password(password):
                return docente
        except Docente.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Docente.objects.get(pk=user_id)
        except Docente.DoesNotExist:
            return None

class NodocenteBackend(BaseBackend):
    def authenticate(self, request, correo=None, password=None, **kwargs):
        try:
            nodocente = Nodocente.objects.get(correo=correo)
            if nodocente.check_password(password):
                return nodocente
        except Nodocente.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Nodocente.objects.get(pk=user_id)
        except Nodocente.DoesNotExist:
            return None