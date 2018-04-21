from django.db import models

# Create your models here.
class UserProfile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    company_name =  models.CharField(max_length=300)
    city = models.CharField(max_length=300)
    state = models.CharField(max_length=300)
    zip = models.PositiveIntegerField()
    email = models.EmailField(max_length=54)
    web = models.URLField(max_length=1000)
    age = models.PositiveIntegerField()

    def __str__(self):
        return ('{} '.format(self.first_name) + ' {}'.format(self.last_name))
