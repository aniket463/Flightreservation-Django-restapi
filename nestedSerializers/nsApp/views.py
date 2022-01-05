from .models import Author,Book
from .serializers import BookSerializer,AuthorSerializer
from rest_framework import generics

#Authentications at class level
# from rest_framework.authentication import BasicAuthentication
# from rest_framework.permissions import IsAuthenticated,DjangoModelPermissions



class AuthorListView(generics.ListCreateAPIView):
    queryset                = Author.objects.all()
    serializer_class        = AuthorSerializer
    # authentications_class   = [BasicAuthentication]
    # permission_classes      = [IsAuthenticated,DjangoModelPermissions]    

class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

