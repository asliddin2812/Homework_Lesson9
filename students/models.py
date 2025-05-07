from django.db import models

# Create your models here.

class Student(models.Model):
    full_name = models.CharField(max_length=100)
    grade = models.IntegerField()
    is_active = models.BooleanField(default=True)
    marks = models.IntegerField(default=0)

    def __str__(self):
        return self.full_name + ' ' + str(self.marks)

    class Meta:
        db_table = 'student'
        ordering = ['full_name']
        verbose_name = 'Student'
        verbose_name_plural = 'Students'




