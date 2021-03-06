from .models import Student
from .serializers import StudentSeializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView 
from django.http import Http404

# class based views
# class StudentList(APIView):

#     def get(self,request):
#         students = Student.objects.all()
#         serializer = StudentSeializer(students,many=True)
#         return Response(serializer.data)
    
#     def post(self,request):
#         serializer = StudentSeializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# class StudentDetail(APIView):
#     def get_object(self,pk):
#         try:
#             return Student.objects.get(pk=pk)
#         except Student.DoesNotExist:
#             raise Http404
    
#     def get(self,request,pk):
#         student = self.get_object(pk)
#         serializer = StudentSeializer(student)
#         return Response(serializer.data)
    
#     def put(self,request,pk):
#         student=self.get_object(pk)
#         serializer=StudentSeializer(student,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self,request,pk):
#         student = self.get_object(pk)
#         student.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
###########################################################################################################################################
# MIXINS

from rest_framework import generics,mixins

# class StudentList(mixins.ListModelMixin,mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSeializer

#     def get(self,request):
#         return self.list(request)

#     def post(self,request):
#         return self.create(request)

# class StudentDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSeializer

#     def get(self,request,pk):
#         return self.retrieve(request,pk)

#     def put(self,request,pk):
#         return self.update(request,pk)
    
#     def delete(self,request,pk):
#         return self.destroy(request,pk)

#########################################################################################################################################
# Generics

# class StudentList(generics.ListCreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSeializer

# class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSeializer

########################################################################################################################
# ViewSet and class level paginations
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination

# class StudentPagination(PageNumberPagination):
#     page_size = 2

# class StudentViewSet(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSeializer
#     # pagination_class = StudentPagination
#     pagination_class = LimitOffsetPagination

#########################################################################################################################
#Djnago custom filtering and search filter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class StudentViewSet(viewsets.ModelViewSet):

    queryset = Student.objects.all()
    serializer_class = StudentSeializer
    pagination_class = LimitOffsetPagination
    # filter_backends  = [DjangoFilterBackend]
    #filter_backends  = [filters.SearchFilter]
    filter_backends  = [filters.OrderingFilter]
    # filterset_fields  = ['name','score']
    #[^,=,@,$]
    #search_fields  = ['=id','=name']
    ordering_fields  = ['name','score']
    ordering = ['score']



   