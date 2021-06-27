from django.db import models

# Create your models here.
class Userregistration(models.Model):
    username = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    mobile = models.IntegerField()
    password = models.CharField(max_length = 20)

    def __str__(self):
        return self.username

    def register(self):
        self.save()

    @staticmethod
    def user_email(email):
        try:
            return Userregistration.objects.get(email = email)
        except:
            return False

    def isExists(self):
        if Userregistration.objects.filter(email = self.email):
            return True
        else:
            return False