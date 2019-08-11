from django.forms import ModelForm
from .models import Pessoa

class PessoaForm(ModelForm):
    class Meta:
        model = Pessoa
        fields=['nome','apelido', 'graduacao', 'peso', 'altura', 'categoria']