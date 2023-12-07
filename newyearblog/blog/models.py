from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField("Название", max_length=100)
    content = models.TextField("Содержание")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"