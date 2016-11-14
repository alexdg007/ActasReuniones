from django.contrib import admin
#from App.models import Lugar, Area, Citacion, Asistente, Tema, Acta, Tarea
#from .views import citaciones, actas, lugares, areas
from Agenda.models import Reuniones, TipoReunion, Lugar, temasdos, EstadoTarea, tareas
from .views import FormularioReuniones, tiposreuniones, lugares, estadosreuniones, temasdosp, temasconsulta
#Administracion
admin.site.register(Lugar, lugares)
admin.site.register(TipoReunion, tiposreuniones)
#admin.site.register(User, usuario)
#admin.site.register(Acta, actas)
# Register your models here.
admin.site.register(temasdos, temasconsulta)
admin.site.register(EstadoTarea)
admin.site.register(tareas)
admin.site.register(Reuniones, FormularioReuniones)
