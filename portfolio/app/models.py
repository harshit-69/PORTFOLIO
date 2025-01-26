from django.db import models



class contacts(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=18)
    message=models.CharField(max_length=500)
    date=models.DateField()

    def __str__(self):
        return self.name
    
