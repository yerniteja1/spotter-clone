from django.db import models

class Candidate(models.Model):
  name = models.CharField(max_length=100)
  email = models.EmailField(unique=True)
  years_experience = models.IntegerField(default=0)
  skills = models.JSONField(default=list)
  
  score = models.FloatField(default=0.0)
  applied_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta():
    ordering = ['-score']
    
  def __str__(self):
    return f"{self.name} - {self.score}"
  
  def save(self, *args, **kwargs):
    self.score = 20
    super().save(*args, **kwargs)