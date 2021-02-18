from django.db import models

# Create your models here.
class MyUsers(models.Model):
    user_id = models.CharField(primary_key=True, max_length=4)
    fName = models.CharField(null=False, max_length=20)
    lName = models.CharField(null=False, max_length=20)
    email = models.CharField(null=False, max_length=40)
    portExistingNumber = models.CharField(null=False, max_length=40)
    password = models.CharField(null=False, max_length=40)
    sharedDocument = models.FileField(null=False)