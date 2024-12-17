from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
import datetime

class DocenteManager(BaseUserManager):
    def create_user(self, correo, contrasena=None):
        if not correo:
            raise ValueError('El usuario debe tener un correo electrónico')
        user = self.model(correo=self.normalize_email(correo))
        user.set_password(contrasena)
        user.save(using=self._db)
        return user

    def create_superuser(self, correo, contrasena):
        user = self.create_user(correo, contrasena)
        user.is_admin = True
        user.save(using=self._db)
        return user

class Docente(AbstractBaseUser, PermissionsMixin):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    rut = models.CharField(max_length=12, unique=True)
    tipo = models.CharField(max_length=20, default='Docente')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='docente_set',  # Añade related_name aquí
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='docente_set',  # Añade related_name aquí
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    objects = DocenteManager()

    USERNAME_FIELD = 'correo'
    REQUIRED_FIELDS = ['nombre', 'rut']

    def __str__(self):
        return self.nombre

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

class EstudianteManager(BaseUserManager):
    def create_user(self, correo, contrasena=None):
        if not correo:
            raise ValueError('El usuario debe tener un correo electrónico')
        user = self.model(correo=self.normalize_email(correo))
        user.set_password(contrasena)
        user.save(using=self._db)
        return user

    def create_superuser(self, correo, contrasena):
        user = self.create_user(correo, contrasena)
        user.is_admin = True
        user.save(using=self._db)
        return user

class Estudiante(AbstractBaseUser, PermissionsMixin):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    rut = models.CharField(max_length=12, unique=True)
    tipo = models.CharField(max_length=20, default='Estudiante')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    asignaturas = models.ManyToManyField('Asignatura', related_name='estudiantes')
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='estudiante_set',  # Añade related_name aquí
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='estudiante_set',  # Añade related_name aquí
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    objects = EstudianteManager()

    USERNAME_FIELD = 'correo'
    REQUIRED_FIELDS = ['nombre', 'rut']

    def __str__(self):
        return self.nombre

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

class NodocenteManager(BaseUserManager):
    def create_user(self, correo, password=None):
        if not correo:
            raise ValueError('El usuario debe tener un correo electrónico')
        user = self.model(correo=self.normalize_email(correo))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, correo, password):
        user = self.create_user(correo, password)
        user.is_admin = True
        user.save(using=self._db)
        return user

class Nodocente(AbstractBaseUser, PermissionsMixin):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    rut = models.CharField(max_length=12, unique=True)
    tipo = models.CharField(max_length=20, default='Nodocente')
    descripcion = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = NodocenteManager()

    USERNAME_FIELD = 'correo'
    REQUIRED_FIELDS = ['nombre', 'rut']

    def __str__(self):
        return self.nombre

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
        
class Asignatura(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    docente = models.ForeignKey(Docente, null=True, blank=True, on_delete=models.SET_NULL, related_name='asignaturas')

    def __str__(self):
        return self.nombre

class Nota(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    nota = models.FloatField()

class Asistencia(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    fecha = models.DateField()
    presente = models.BooleanField()

class Anotacion(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE)
    fecha = models.DateField(default=datetime.date.today)
    descripcion = models.TextField()

    def __str__(self):
        return f"Anotación de {self.estudiante.nombre} por {self.docente.nombre} el {self.fecha}"

class Evento(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha = models.DateField()

    def __str__(self):
        return self.nombre

class Reclamo(models.Model):
    estudiante = models.ForeignKey('Estudiante', on_delete=models.CASCADE)
    docente = models.ForeignKey('Docente', on_delete=models.CASCADE)
    descripcion = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Reclamo de {self.estudiante.nombre} contra {self.docente.nombre}'