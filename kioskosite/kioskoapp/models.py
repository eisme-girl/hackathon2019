from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm

# Create your models here.

class Perfil (models.Model):
    dinero = models.DecimalField(default=0.00,decimal_places=2,max_digits=6)
    pase_anual = models.BooleanField(default=False)
    usuario = models.OneToOneField(User,on_delete=models.CASCADE)

class PerfilForm(ModelForm):
    class Meta:
        model=Perfil
        fields = ['dinero', 'pase_anual']

class Tag (models.Model):
    perfil = models.ForeignKey(Perfil,on_delete=models.CASCADE,default=None)
    fp= models.IntegerField(default=1)  
    
class TagForm(ModelForm):
    class Meta:
        model=Tag
        fields = ['fp']
