from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Course(models.Model):
  course_name = models.CharField(max_length=101)
  description_name = models.CharField(max_length=100)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)

  