from django.db import models

# Create your models here.
class Champion(models.Model):

    name = models.CharField(max_length=100)
    img = models.CharField(max_length=550)
    bio = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        
class Abilities(models.Model):
    ultimate = models.CharField(max_length=150)
    skill1 = models.CharField(max_length=150)
    skill2 = models.CharField(max_length=150)
    health = models.IntegerField(default=0)
    champion = models.ForeignKey(Champion, on_delete=models.CASCADE, related_name='abilities')
    
    def __str__(self):
        return self.ultimate
    