from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager, models.Manager):

    def _create_user(self, username, email, password, is_staff, is_superuser, **extra_fields):

        email = self.normalize_email(email)
        if not email:
            raise ValueError("el email es obligatorio")

        user = self.model(
            username=username,
            email=email,
            is_active=True,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, password=None, **extra_fields):
        return self._create_user(
            username, email, password, False, False, **extra_fields
        )

    def create_superuser(self, username, email, password=None, **extra_fields):
        return self._create_user(
            username, email, password, True, True, **extra_fields
        )


class User(AbstractBaseUser, PermissionsMixin):

    GENDER_CHOICES = (
        ('M', 'MASCULINO'),
        ('F', 'FEMENINO'),
    )
    username = models.CharField('username', max_length=8, unique=True)
    email = models.EmailField('correo electronico')
    first_name = models.CharField('nombres', max_length=50)
    last_name = models.CharField('apellidos', max_length=50)
    avatar = models.ImageField(upload_to='users')
    address = models.CharField('direccion', max_length=50)
    phone = models.CharField('telefono', max_length=50)
    gender = models.CharField('sexo', max_length=1, choices=GENDER_CHOICES)

    objects = UserManager()

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return "%s %s" % (self.first_name, self. last_name)
