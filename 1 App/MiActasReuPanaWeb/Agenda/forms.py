from django import forms
#from App.models import Lugar, Area, Citacion, Asistente, Tema, Acta, Tarea
#from django.forms import ModelForm
from Agenda.models import Lugar, Reuniones
from django.forms import ModelForm


#Form Citaciones
class RegisReuniones(forms.ModelForm):
	#def __init__(self, *args, **kwargs):
	#	super(RegisCitacion, self).__init__(*args, **kwargs)
	#	self.list_display['citacion_id', 'organizador', 'asunto', 'fecha_hora', 'lugar', 'temas', 'estado'].queryset = Citacione.objects.filter(estado='Activa')

	class Meta:
		model = Reuniones
		fields = ('organizador', 'idTipo', 'idLugar', 'tiempo_estimado', 'asunto')

		def __init__(self):
			print (self.cleaned_data)
