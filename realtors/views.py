from django.shortcuts import render
from .models import Realtor
from .serializers import RealtorSerializer
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
#no need of these two cause we have added it globally
#from rest_framework.authentication import BasicAuthentication 
#from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions



 
class StudentPagination(PageNumberPagination):
	page_size = 2


class RealtorViewSet(viewsets.ModelViewSet):
	queryset = Realtor.objects.all()
	serializer_class = RealtorSerializer
	pagination_class = LimitOffsetPagination
	#authentication_classes = [BasicAuthentication]
	#permission_classes  = [IsAuthenticated, DjangoModelPermissions]
