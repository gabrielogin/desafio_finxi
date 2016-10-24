from django import forms

from .models import Imovel

class ImovelForm(forms.ModelForm):

    class Meta:
        model = Imovel
        fields = ('nome', 'descricao','endereco','cidade','estado','imovel','valor','imagem')
