from django.db import models

# Create your models here.
class employee(models.Model):
    employee_id  = salary= models.IntegerField()
    first_name   = models.CharField(max_length=200)
    last_name    = models.CharField(max_length=200)
    job_title    = models.CharField(max_length=200)
    salary       = models.IntegerField()
    reports_to   = models.CharField(max_length=200)
    office_id    = models.IntegerField()