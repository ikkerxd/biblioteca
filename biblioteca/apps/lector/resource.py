from import_export import resources
from .models import Lector


class LectorResource(resources.ModelResource):

    class Meta:
        model = Lector
        import_id_fields = ('Codigo',)
        fields = ('Codigo', 'dni', 'nombres', 'apellidos', 'sexo', 'tipo__nombre')