from django.db import models
from account.models import Userregistration

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length = 100)
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to="image/",null= False, blank = False)
    icon = models.ImageField(upload_to ="image/")
    votes_total = models.IntegerField(default=1)
    body = models.TextField()
    url = models.TextField()
    rating = models.ForeignKey(Userregistration, on_delete=models.CASCADE)

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e, %y')
        
    def __str__(self):
        return self.title