# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
#
from django import forms
from django.contrib import admin
#from App.models import Lugar, Area, Citacion, Asistente, Tema, Acta, Tarea, PuenteActaTema
#from .forms import RegisCitacion, RegisActa
from django.forms.models import BaseInlineFormSet
#from django.forms import BaseFormSet
from django.forms import formset_factory
from django.core.mail import send_mail
from django_admin_bootstrapped.admin.models import SortableInline
from django_admin_bootstrapped.widgets import GenericContentTypeSelect
from django.forms.widgets import CheckboxSelectMultiple
from Agenda.models import Lugar, Reuniones, TipoReunion, EstadoTarea, temasdos, asistentes, tareas
from .forms import RegisReuniones
# Create your views here.
from django.contrib.auth.models import User
from django.forms import BaseFormSet, BaseModelFormSet
from django.forms import formset_factory, modelformset_factory


#class FormularioReuniones(admin.ModelAdmin):
#	form = RegisReuniones #Generar un orden de visualizacion
#	inlines = (Temas, ) #Bloques detalle otros asistentes y compromisos
class AsistInLineFormSet(BaseInlineFormSet):
	"""docstring for AsistInLineFormSet"""
	def clean(self):
		super(AsistInLineFormSet, self).clean()
		#formCita = RegisCitacion(request.POST or None)
		total = 0
		for form in self.forms:
			if not form.is_valid():
				return #
			if form.cleaned_data and not form.cleaned_data.get('DELETE'):
			#if form.cleaned_data and formCita.cleaned_data:
				nombre = form.cleaned_data['user']
				correo = form.cleaned_data['email']
				#asunto = formCita.cleaned_data['asunto']
				#if  '@unipanamericana.edu.co' not in correo:
				#	raise forms.ValidationError("Por favor solo se admiten correos con el dominio @unipanamericana.edu.co")
				#else:
				print(correo)
				cita = 'Estimado Sr. '
				info = ", Usted ha sido Citado a una Reunion, "
				info1 = "El lugar de la reunion es la Sala Gis "
				info2 = "El dia 08/11/2016 a las 21:27:34 "
				info3 = "Temas a Tratar: Verificar item gis, Verificar item gis 2 "
				inf  = " para conocer mas detalles acerca de la Reunion Por Favor ingrese a la siguiente URL http://127.0.0.1:8000/ReunionesActasPana/"
				msg = cita + str(nombre) + info + inf
				#send_mail('Citacion Reunion', msg, 'adguzman@unipanamericana.edu.co', [correo], fail_silently=False)

class TemasInLineFormSet(BaseInlineFormSet):
	"""docstring for TemasInLineFormSet"""
	def clean(self):
		super(TemasInLineFormSet, self).clean()
		#formCita = RegisCitacion(request.POST or None)
		total = 0
		for form in self.forms:
			if not form.is_valid():
				return #
			if form.cleaned_data and not form.cleaned_data.get('DELETE'):
				nombre = form.cleaned_data['nombre']
				print(nombre)



class ReuBaseFormSet(BaseModelFormSet):
	def clean(self):
		super(ReuBaseFormSet, self).clean()
		#formCita = RegisCitacion(request.POST or None)
		total = 0
		for form in self.forms:
			if not form.is_valid():
				return #
			if form.cleaned_data and not form.cleaned_data.get('DELETE'):
			#if form.cleaned_data and formCita.cleaned_data:
				org = form.cleaned_data['organizador']
				#asunto = formCita.cleaned_data['asunto
				print(org)

class lugares(admin.ModelAdmin):
	fields = ('descripcion', )


class tiposreuniones(admin.ModelAdmin):
	fields = ('descripcion', )

class estadosreuniones(admin.ModelAdmin):
	fields = ('NombreEstado', )

#class asistentesreunion(admin.StackedInline, SortableInline):
class asistentesreunion(admin.TabularInline):
	model = asistentes
	#user = request.user.get_full_name()
	formset = AsistInLineFormSet
	fields = ('user', 'email')
	#fields = ('user', 'email', 'asiste', 'firma')
	extra = 0

	def formfield_for_foreignkey(self, db_field, request, **kwargs):
		if db_field.name == 'user':
			kwargs['queryset'] = User.objects.filter(is_active='t').order_by('first_name')
		return super(asistentesreunion, self).formfield_for_foreignkey(db_field, request, **kwargs)

	#def formfield_for_foreignkey(self, db_field, request, **kwargs):
	#	if db_field.name == 'first_name':
	#		kwargs['queryset'] = User.objects.filter(is_active='t').order_by('first_name')
	#	return super(asistentesreunion, self).formfield_for_foreignkey(db_field, request, **kwargs)


#class envio_correo:
#	asistentes[AsistInLineFormSet]
#	for i in []:
#		send_mail('Citacion Reunion', 'Prueba correos', 'adguzman@unipanamericana.edu.co', [asistentes], fail_silently=False)

#class TareasReu(admin.TabularInline):
class TareasReu(admin.StackedInline, SortableInline):
	model = tareas
	fields = ('nombretarea', 'descripcion', 'resposable', 'fecha_limite', 'observaciones', 'IdEstadoTarea')
	extra = 0

	def formfield_for_foreignkey(self, db_field, request, **kwargs):
		if db_field.name == 'resposable':
			kwargs['queryset'] = asistentes.objects.filter(idReunion=1)
		return super(TareasReu, self).formfield_for_foreignkey(db_field, request, **kwargs)

#class temasdosp(admin.TabularInline):
class temasdosp(admin.StackedInline, SortableInline):
	model = temasdos
	formset = TemasInLineFormSet
	raw_id_fields = ('tema_padre_dos',)
	fields = ('nombre', 'tema_padre_dos')
	#fields = ('nombre', 'Contenido', 'Acuerdos', 'tema_padre_dos')
	extra = 0


class FormularioReuniones(admin.ModelAdmin):
	form = RegisReuniones
	#model = Reuniones

	formset = ReuBaseFormSet
	inlines = [
		temasdosp, asistentesreunion, TareasReu
		#temasdosp, asistentesreunion,
		]
		#exclude = ('idTema',)
	fieldsets = (
		('Agendamiento y Registro de Reunión', {
			'fields': ['organizador', 'fecha_hora', 'idTipo', 'idLugar', 'tiempo_estimado', 'hora_final', 'asunto', 'idEstado'] #'citacion',
		}),
		#('Temas, Contenido, Acuerdos', {
		#    'classes': ('collapse',),
		#    'fields': ('temas', 'contenido', 'acuerdos',),
		#}),
	)
	#ReunionesFormSet = formset_factory(RegisReuniones, formset=BaseReunionesFormset)
	#ReuFormSet = modelformset_factory(Reuniones, fields=('organizador',))
	#formset = ReuFormSet()
	#print(ReuFormSet)
	#formset = formBase
	#save_on_top = True -> Agregar botones en parte superior
	list_display = ['organizador',  'asunto', 'fecha_hora', 'idTipo', 'idLugar', 'tiempo_estimado', 'hora_final', 'link',]
	list_display_links =['organizador',]
	search_fields = ['organizador', 'fecha_hora', 'tiempo_estimado', 'hora_final', 'asunto']
	list_filter = ['organizador', 'fecha_hora', 'idTipo', 'idLugar', ]
	#enviar = envio_correo
	#raw_id_fields = ['citacion_id'] #Buscar por el numero de acta
	def clean(self):
		super(FormularioReuniones, self).clean()
		#formCita = RegisCitacion(request.POST or None)
		total = 0
		for form in self.forms:
			if not form.is_valid():
				return #
			if form.cleaned_data and not form.cleaned_data.get('DELETE'):
			#if form.cleaned_data and formCita.cleaned_data:
				org = form.cleaned_data['organizador']
				#asunto = formCita.cleaned_data['asunto
				print(org)
				return self.org


#configuracion para consulta de temas
class temasconsulta(admin.ModelAdmin):
	model = temasdos
	list_display = ['nombre', 'Contenido', 'Acuerdos', ]
	search_fields = ['nombre', 'Contenido', 'Acuerdos',]
