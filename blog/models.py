##What are the characteristics of a typical blog application? 
# In our case, let’s keep things simple and assume each post has a title, author, and body. 
# We can turn this into a database model by opening the blog/models.py file and entering the code below:

from django.db import models
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        "auth.user",
        on_delete=models.CASCADE,
    )
    body = models.TextField()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})

