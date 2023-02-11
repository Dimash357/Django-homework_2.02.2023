from django.db import models

class Post(models.Model):
    title = models.CharField(
        verbose_name="Заголовок",
        default="",
        editable=True,
        blank=True,
        unique=True,
        db_index=True,

        max_length=150
    )
    description = models.TextField(
        verbose_name="Описание",
        default="",
        editable=True,
        blank=True
    )

    class Meta:
        app_label = 'django_app'
        ordering = ('id',)
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'

    def __str__(self):
        return f"Post: {self.title} {self.description[:30]} [{self.pk}]"