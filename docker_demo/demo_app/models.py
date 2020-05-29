from django.db import models

# Create your models here.
class Employee(models.Model):
	name = models.CharField(max_length = 50)
	age = models.IntegerField(default = 0)
	salary = models.FloatField(default = 0)

	class Meta:
		db_table = 'employee_tbl'