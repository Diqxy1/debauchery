# Generated by Django 3.2.4 on 2021-06-30 22:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coachs', '0003_auto_20210622_1446'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coach',
            options={'ordering': ['id'], 'verbose_name': 'coach', 'verbose_name_plural': 'coachs'},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ['id'], 'verbose_name': ('Avaliação',), 'verbose_name_plural': 'Avaliações'},
        ),
    ]
