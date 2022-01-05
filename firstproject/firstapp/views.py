from django.shortcuts import render
from django.http import JsonResponse
from .models import Employee

# Create your views here.
def employeeView(request):
    # emp = {
    #     'id':123,
    #     'name':'Aniket',
    #     'sel':250000,
    # }

    data = Employee.objects.all()
    response = {
        'employee':list(data.values('name','sal'))
    }
    return JsonResponse(response)
