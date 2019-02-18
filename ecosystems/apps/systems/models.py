from django.db import models



# Create your models here.

class Accesses(models.Model):
    """

    """
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    service = models.CharField(max_length=100)
    login = models.CharField(max_length=30)
    password = models.CharField(max_length=500)
    comment = models.CharField(max_length=150)
    owner = models.CharField(max_length=30)

    def __str__(self):
        return self.login
