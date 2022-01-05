from rest_framework import serializers
from .models import Student

class StudentSeializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','name','score']