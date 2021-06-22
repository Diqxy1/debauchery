from django.db import models


class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Coach(Base):
    title = models.CharField(max_length=120)
    description = models.TextField(max_length=1000)
    url = models.URLField(unique=True)

    class Meta:
        verbose_name = 'coach'
        verbose_name_plural = 'coachs'

    def __str__(self):
        return self.title


class Assessment(Base):
    coach = models.ForeignKey(Coach, related_name='avaliacoes', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    comment = models.TextField(blank=True, default='')
    valuation = models.DecimalField(max_digits=2, decimal_places=1)

    class Meta:
        verbose_name = 'Avaliação',
        verbose_name_plural = 'Avaliações'
        unique_together = ['email', 'coach']

    def __str__(self):
        return f'{self.name} avaliou o curso {self.coach} com nota {self.valuation}'
