from django.forms import ModelForm
from .models import peliculas

class TaskForm(ModelForm):
    class Meta:
        model = peliculas
        fields = ['titulo', 'descripcion','importante','genero', 'director']