from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    create_on = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return self.title 

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=100)
    email = models.EmailField()
    create_on = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    active = models.BooleanField(default=False)
    def __str__(self):
        return f"Comentario de {self.name} en [{self.post}]"

