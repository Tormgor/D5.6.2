from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('Author', null=True, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.title.title()} : {self.description}'

    def get_absolute_url(self):
        return f'/news/{self.id}'


class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name}'