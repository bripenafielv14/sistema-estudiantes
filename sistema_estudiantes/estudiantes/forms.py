from django import forms
from .models import Estudiante


class EstudianteForm(forms.ModelForm):

    class Meta:
        model = Estudiante
        fields = ['nombre', 'apellido', 'edad', 'correo', 'carrera', 'semestre']

    def clean_edad(self):
        edad = self.cleaned_data['edad']

        if edad < 1:
            raise forms.ValidationError('La edad debe ser mayor que 0.')

        return edad

    def clean_semestre(self):
        semestre = self.cleaned_data['semestre']

        if semestre < 1 or semestre > 10:
            raise forms.ValidationError(
                'El semestre debe estar entre 1 y 10.'
            )

        return semestre