from django.contrib import admin
from .models import Perfil,Tag
# Register your models here.

class PerfilAdmin(admin.ModelAdmin):
    pass
class TagAdmin(admin.ModelAdmin):
    pass


admin.site.register(Perfil, PerfilAdmin)
admin.site.register(Tag,TagAdmin)