from django.contrib import admin
from .models import Post
# Register your models here.

@admin.register(Post)
#mostra os campos na pagina de admin
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "author", "created", "updated")
    #preenche o campos slug automaticamente conforme o preenchimento do title
    prepopulated_fields = {"slug":("title", )}