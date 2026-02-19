from django.db import models

# Create your models here.

class Info(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    salary = models.FloatField()
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} ({self.email})"
    
    class Meta:
        verbose_name = "User Info"
        verbose_name_plural = "Users Info"
        ordering = ['-created_at']