from django.db import models
from django.contrib.auth.models import User


STATUS = (
    (0, 'Draft'),
    (1, 'Publish')
)

# CRIAR TABELA NO CANDO DE DADOS 
class Post(models.Model):
    title = models.CharField(max_length= 200, unique= True) # Tabela de titulo do post
    slug = models.SlugField(max_length= 200, unique= True) # Tabela de titulo do slug
    author = models.ForeignKey(User, on_delete= models.CASCADE, related_name= 'post_postfolio') # Tabela de titulo do com nome do author
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add= True)
    status = models.IntegerField(choices= STATUS, default=0)


    class Meta:
        ordering = ['-created_on'] # Essa class deixa a ordem dos post decrecente 


    def __str__(self):
        return self.title