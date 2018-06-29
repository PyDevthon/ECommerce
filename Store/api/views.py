from rest_framework import generics
from rest_framework.views import APIView
from .serializers import ContactSerializers
from ..models import Contact


class ContactCreteView(generics.ListCreateAPIView):
    serializer_class = ContactSerializers
    queryset = Contact.objects.all()


