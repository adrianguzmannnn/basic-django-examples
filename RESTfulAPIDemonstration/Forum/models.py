from django.db import models

class Post(models.Model):

    # pk: Django creates an auto-incrementing integer primary key by default.
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"

    def get_comments(self):
        return self.comment_set.all().order_by("-updated_at")


class Comment(models.Model):
    
    # pk: Django creates an auto-incrementing integer primary key by default.
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return f"{self.body}"
