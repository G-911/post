from django.db import models
from django.urls import reverse

# Create your models here.


class Post(models.Model):
    tittle = models.CharField(max_length=30)
    author = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
    )

    body = models.TextField()

    def __str__(self):
        return self.tittle
    
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
