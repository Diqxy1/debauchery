from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator


class User(AbstractBaseUser, PermissionsMixin):
    class AccessLevel(models.IntegerChoices):
        ADMINISTRATOR = 0, 'Administrador'
        MODERATOR = 1, 'Moderator'
        COACH = 2, 'Coach'
        USER = 3, 'User'

    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        'usuário',
        max_length=150,
        unique=True,
        help_text='Obrigatório. no máximo 80 caracteres. Letras, Dígitos e @/./+/-/_',
        validators=[username_validator],
        error_messages={
            'unique': "Esse nome de usuário já está em uso",
        },
    )
    email = models.EmailField('e-mail', blank=True, null=True)
    is_staff = models.BooleanField(
        'pertence a administração',
        default=False,
        help_text='Usuário com acesso ao painel gerald e administração',
    )
    is_active = models.BooleanField(
        'ativo',
        default=True,
        help_text='Status do usuário para permissão de login'
    )
    access_level = models.IntegerField('nível de acesso', choices=AccessLevel.choices, default=AccessLevel.USER,
                                       blank=True)
    # timestamps
    created_at = models.DateTimeField('data de criação', auto_now_add=True)
    updated_at = models.DateTimeField('data de atualização', auto_now=True)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'access_level']

    class Meta:
        verbose_name = 'usuário'
        verbose_name_plural = 'usuários'

    def __str__(self):
        return self.username
