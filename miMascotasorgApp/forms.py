from django import forms


class FormularioContacto(forms.Form):
    nombre=forms.CharField(max_length=50, widget=forms.TextInput(attrs= {'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
                             'class': 'form-control', 'placeholder': 'ejemplo@ejemplo.com'}), label="Email", error_messages={'blank': 'Por favor escriba su email', 'null': 'Por favor escriba su email', 'invalid': 'Escribe un email válido'})
    mensaje = forms.CharField(required=True, widget=forms.Textarea(
        attrs={'rows': 6, 'class': 'form-control', 'placeHolder':"Comentarios..."}), error_messages={'blank': 'Por favor escriba su email', 'null': 'Por favor escriba su email', 'invalid': 'Escribe un email válido'})