from django.db import models

# Create your models here.

# Will accept data from home form 
class Candidates(models.Model):
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    catagory = models.CharField(max_length=10)
    course = models.CharField(max_length=300)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Candidates"


# Admin can add courses 
class Courses(models.Model):
    course_name = models.CharField(max_length=300)

    def __str__(self):
        return self.course_name

    class Meta:
        verbose_name_plural = "Courses"    