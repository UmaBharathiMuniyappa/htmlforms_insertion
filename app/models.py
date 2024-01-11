from django.db import models

# Create your models here.
class School(models.Model):
    sname=models.CharField(max_length=100,primary_key=True)
    sloc=models.CharField(max_length=100)
    sprinci=models.CharField(max_length=100)

    def __str__(self):
        return self.sname

class Student(models.Model):
    sid=models.IntegerField(primary_key=True)
    sname=models.ForeignKey(School,on_delete=models.CASCADE)
    stname=models.CharField(max_length=100)
    stphone=models.IntegerField()
 
    def __str__(self):
        return self.stname