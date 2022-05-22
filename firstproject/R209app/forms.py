from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class tableauxForm(ModelForm):
    class Meta:
        model = models.tableaux
        fields = ('titre', 'peintre', 'date_parution', 'mouvement_artistique', 'idee')
        labels = {
            'titre' :_('Titre'),
            'peintre' :_('Peintre'),
            'date_parution' :_('Date de parution'),
            'mouvement_artistique' :_('Mouvement artistique'),
            'idee' :_('Idée'),
        }

