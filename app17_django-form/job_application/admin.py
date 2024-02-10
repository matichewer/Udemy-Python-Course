from django.contrib import admin
from .models import Form

# Register your models here.


class FormAdmin(admin.ModelAdmin):
    # campos a mostrar
    list_display = ("first_name", "last_name", "email", "date", "occupation")
    
    # busqueda
    search_fields = ("first_name", "last_name", "email", "date", "occupation")
    
    # filtros
    list_filter = ("date", "occupation")
    
    # ordenando en reversa
    ordering = ("-first_name", )
    

admin.site.register(Form, FormAdmin)

