from django.db import models

class Student (models.Model):
   ID = models.CharField(max_length=20)
   LastName = models.CharField(max_length=20)
   FirstName = models.CharField(max_length=20)
   State = models.CharField(max_length=20)
   Gender = models.CharField(max_length=20)
   StudentStatus = models.CharField(max_length=20)
   Major = models.CharField(max_length=20)
   Country = models.CharField(max_length=20)
   Age = models.CharField(max_length=20)
   SAT = models.CharField(max_length=20)
   Grade = models.CharField(max_length=20)
   Height = models.CharField(max_length=20)
   
   def __str__(self) -> str:
      return "%s" %(self.LastName)
  
  
   class Meta: 
        db_table = "Students"
      