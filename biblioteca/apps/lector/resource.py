# -*- coding: utf-8 -*-
from import_export import resources, fields
from .models import Lector, CarreraProfesional, TipoLector
from import_export.widgets import ForeignKeyWidget
from import_export.admin import ImportExportModelAdmin


class LectorResource(resources.ModelResource):
    carrera = fields.Field(column_name='carrera__codigo', attribute='carrera', widget=ForeignKeyWidget(CarreraProfesional, 'codigo'))
    tipo = fields.Field(column_name='tipo__nombre', attribute='tipo', widget=ForeignKeyWidget(TipoLector, 'nombre'))
    class Meta:
    	fields = ('id','codigo', 'dni','apellidos_y_nombres','fecha_inicio','fecha_fin','tipo','carrera') #el orden es: carrera,tipo,id,apellidos y nombres, codigo, dni
        model = Lector


