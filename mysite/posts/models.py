from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Posts(models.Model):
    text = models.TextField()
    pud_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата публикации"
    )
    author = models.ForeignKey(
        User,
        verbose_name='Автор',
        on_delete=models.CASCADE,
        related_name='posts'
    )
    image = models.ImageField(
        upload_to= "posts/",
        blank=True,
        verbose_name="Фото",
    )