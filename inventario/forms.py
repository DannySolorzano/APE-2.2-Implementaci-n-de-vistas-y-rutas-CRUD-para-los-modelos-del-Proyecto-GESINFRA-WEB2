from django import forms
from .models import Equipo

class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = ['numero_inventario', 'descripcion', 'precio_adquisicion']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Agregar clases CSS para estilización
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'placeholder': f'Ingrese {self.fields[field].label.lower()}'
            })
        
        # Personalizar etiquetas
        self.fields['numero_inventario'].label = "Número de Inventario"
        self.fields['descripcion'].label = "Descripción del Equipo"
        self.fields['precio_adquisicion'].label = "Precio de Adquisición ($)"