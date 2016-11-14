# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-11-14 01:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='asistentes',
            fields=[
                ('idasis', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(blank=True, default='@unipanamericana.edu.co', max_length=50, null=True, verbose_name='Correo')),
                ('asiste', models.CharField(blank=True, choices=[('S', 'SI'), ('N', 'NO')], max_length=2, null=True, verbose_name='Asiste')),
                ('firma', models.CharField(blank=True, choices=[('S', 'SI'), ('N', 'NO')], max_length=2, null=True, verbose_name='Firma')),
            ],
            options={
                'verbose_name_plural': 'Asistentes',
                'verbose_name': 'Asistente',
            },
        ),
        migrations.CreateModel(
            name='EstadoReunion',
            fields=[
                ('idEstado', models.AutoField(primary_key=True, serialize=False)),
                ('NombreEstado', models.CharField(max_length=100)),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('usuario_creador', models.CharField(max_length=50)),
                ('fecha_modificacion', models.DateField(auto_now=True)),
                ('usuario_modificador', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': '3. Estado Reuniones',
                'verbose_name': 'Estado Reunion',
            },
        ),
        migrations.CreateModel(
            name='EstadoTarea',
            fields=[
                ('IdEstadoTarea', models.AutoField(primary_key=True, serialize=False)),
                ('NomEstadoTar', models.CharField(blank=True, max_length=100, null=True, verbose_name='Estado Tarea')),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('usuario_creador', models.CharField(max_length=50)),
                ('fecha_modificacion', models.DateField(auto_now=True)),
                ('usuario_modificador', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': '4. Estado Tareas',
                'verbose_name': '4. Estado Tarea',
            },
        ),
        migrations.CreateModel(
            name='Lugar',
            fields=[
                ('idLugar', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=50)),
                ('Estado', models.CharField(choices=[('S', 'Disponible'), ('N', 'No Disponible')], max_length=1, null=True)),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('usuario_creador', models.CharField(max_length=50)),
                ('fecha_modificacion', models.DateField(auto_now=True)),
                ('usuario_modificador', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': '2. Lugares',
                'verbose_name': 'Lugar',
            },
        ),
        migrations.CreateModel(
            name='padrereuniones',
            fields=[
                ('padre', models.AutoField(primary_key=True, serialize=False)),
                ('reunion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Reuniones',
            fields=[
                ('IdReunion', models.AutoField(primary_key=True, serialize=False, verbose_name='Numero de Citacion')),
                ('organizador', models.CharField(max_length=50)),
                ('fecha_hora', models.DateTimeField()),
                ('tiempo_estimado', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], help_text='Numero de Horas', null=True)),
                ('asunto', models.CharField(max_length=100)),
                ('hora_final', models.TimeField(help_text='HH24:MM:SS')),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('usuario_creador', models.CharField(max_length=50)),
                ('fecha_modificacion', models.DateField(auto_now=True)),
                ('usuario_modificador', models.CharField(max_length=50)),
                ('idEstado', models.ForeignKey(blank=True, max_length=2, null=True, on_delete=django.db.models.deletion.CASCADE, to='Agenda.EstadoReunion', verbose_name='Estado Reunion')),
                ('idLugar', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Agenda.Lugar', verbose_name='Lugar Reunion')),
            ],
            options={
                'verbose_name_plural': 'Reuniones',
                'verbose_name': 'Reunion',
            },
        ),
        migrations.CreateModel(
            name='tareas',
            fields=[
                ('idTarea', models.AutoField(primary_key=True, serialize=False)),
                ('nombretarea', models.CharField(blank=True, max_length=4000, null=True, verbose_name='Nombre Tarea')),
                ('descripcion', models.TextField(max_length=4000)),
                ('fecha_limite', models.DateField()),
                ('observaciones', models.TextField(max_length=4000)),
                ('IdEstadoTarea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Agenda.EstadoTarea', verbose_name='Estado Tarea')),
                ('idReunion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Agenda.Reuniones')),
                ('resposable', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Agenda.asistentes', verbose_name='Responsable')),
            ],
            options={
                'verbose_name_plural': '7. Tareas',
                'verbose_name': 'Tarea',
            },
        ),
        migrations.CreateModel(
            name='temasdos',
            fields=[
                ('tema', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre Tema')),
                ('Contenido', models.TextField(blank=True, max_length=4000, null=True)),
                ('Acuerdos', models.TextField(blank=True, max_length=4000, null=True)),
                ('idreunion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Agenda.Reuniones')),
                ('tema_padre', models.ManyToManyField(blank=True, null=True, related_name='_temasdos_tema_padre_+', to='Agenda.temasdos')),
                ('tema_padre_dos', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Agenda.temasdos', verbose_name='Tema a Asociar')),
            ],
            options={
                'verbose_name_plural': '5. Temas',
                'verbose_name': 'Tema',
            },
        ),
        migrations.CreateModel(
            name='TipoReunion',
            fields=[
                ('idTipo', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=50)),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('usuario_creador', models.CharField(max_length=50)),
                ('fecha_modificacion', models.DateField(auto_now=True)),
                ('usuario_modificador', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': '1. Tipos Reuniones ',
                'verbose_name': 'Tipo Reunion',
            },
        ),
        migrations.AddField(
            model_name='reuniones',
            name='idTipo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Agenda.TipoReunion', verbose_name='Tipo Reunion'),
        ),
        migrations.AddField(
            model_name='asistentes',
            name='idReunion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Agenda.Reuniones'),
        ),
        migrations.AddField(
            model_name='asistentes',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Asistente'),
        ),
    ]