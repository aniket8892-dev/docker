from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from .models import *

class Home(View):
	def get(self, request, *args, **kwargs):
		employee_list = Employee.objects.all()
		return render(request, "homepage.html",{"employee_list":employee_list})