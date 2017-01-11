from django.db import models
from django import forms

# Create your models here.

class Build(models.Model):
    titre = models.CharField(max_length=100)
    prof = models.CharField(max_length=20)
    contenu = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True, auto_now=False, 
                                verbose_name="Date de parution")
    
    def __str__(self):
        """ 
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que 
        nous traiterons plus tard et dans l'administration
        """
        return self.titre

class BuildForm(forms.ModelForm):
    class Meta:
        model = Build
        fields = '__all__'