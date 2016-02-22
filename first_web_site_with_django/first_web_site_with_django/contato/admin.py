from django.contrib import admin
from first_web_site_with_django.contato.models import Contato, Tarefas


class ContatoAdmin(admin.ModelAdmin):
    model = Contato
    list_display = ['contato_nome', 'contato_email', 'contato_favorito']
    list_filter = ['contato_sexo', 'contato_estado_civil']
    search_fields = ['contato_nome']
    save_on_top = True
admin.site.register(Contato, ContatoAdmin)

class TarefaAdmin(admin.ModelAdmin):
    model = Tarefas
    list_display = ['tarefa_nome', 'tarefa_data_inicio', 'concluido']
    search_fields = ['tarefa_nome']
    save_on_top = True
admin.site.register(Tarefas, TarefaAdmin)
