from django.db import models

# Create your models here.



 
class studentInfo(models.Model):

    status_choies ={
        ("Python","Python"),
        ("Django","Django"),
         ("Flutter","Flutter")
    }  
    
    studentName = models.CharField(max_length=250)
    studentID = models.CharField(max_length=250)
    subject = models.CharField(choices= status_choies,max_length=250,default="----")


    def __str__(self) :
        return self.studentName

     




 