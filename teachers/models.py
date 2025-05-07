from django.db import models

# Create your models here.
class Teacher(models.Model):
    subject_choice = [
        ('math', 'Math'),
        ('physics', 'Physics'),
        ('english', 'English'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    experience_year = models.FloatField()
    subject = models.CharField(max_length=100, choices=subject_choice,null=True,blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'teacher'
        ordering = ['name']
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'
