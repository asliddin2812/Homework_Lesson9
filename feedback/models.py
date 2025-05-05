from django.db import models

# Create your models here.
class Feedback(models.Model):
    student_name = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.student_name
    class Meta:
        db_table = 'feedback'
        ordering = ['student_name']
        verbose_name = 'Feedback'
        verbose_name_plural = 'Feedbacks'

