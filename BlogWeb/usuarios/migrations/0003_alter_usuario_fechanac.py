# Generated by Django 4.1.4 on 2022-12-12 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_usuario_fechanac'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='fechaNac',
            field=models.DateField(default=None, null=True),
        ),
    ]
