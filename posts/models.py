from django.db import models

# Create your models here.
class Post(models.Model):
    caption = models.CharField(
        max_length=300,     #DB column will be VARCHAR(300)
        blank=True,         # caption is optional ; empty string allowed
    )

    # Where the image lives for now (can be a CDN or normal URL)
    image_url = models.URLField()

    # Auto-filled when the row is first created
    created_at = models.DateTimeField(auto_now_add=True)

    # Lets you "hide" a post without deleting it from the DB
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        #human-readable name in admin / shell
        return self.caption[:50] or f"Post {selk.pk}"
