from django.db import models

class Pipeline(models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=50, choices=[('SUCCESS', 'Success'), ('FAILED', 'Failed'), ('RUNNING', 'Running')],default='RUNNING',)
    last_run = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Step(models.Model):
    pipeline = models.ForeignKey(Pipeline, related_name='steps', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('success', 'Success'), ('failed', 'Failed')])
    order = models.IntegerField()

    def __str__(self):
        return f"{self.order} - {self.name} ({self.status})"

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.BooleanField(default=False)  # True = completed, False = not completed

    def __str__(self):
        return self.title