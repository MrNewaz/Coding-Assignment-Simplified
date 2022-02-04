from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, RetrieveAPIView, UpdateAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.viewsets import ModelViewSet
from .serializers import *
from .models import *


# Parent ViewSet
class ParentListApiView(ListAPIView):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer


class ParentCreateApiView(CreateAPIView):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer


class ParentDestroyApiView(DestroyAPIView):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer
    lookup_field = 'id'


class ParentUpdateApiView(UpdateAPIView):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        return Response(serializer.data)


# Child ViewSet
class ChildListApiView(ListAPIView):
    queryset = Child.objects.all()
    serializer_class = ChildSerializer


class ChildCreateApiView(CreateAPIView):
    queryset = Child.objects.all()
    serializer_class = ChildSerializer


class ChildDestroyApiView(DestroyAPIView):
    queryset = Child.objects.all()
    serializer_class = ChildSerializer
    lookup_field = 'id'


class ChildUpdateApiView(UpdateAPIView):
    queryset = Child.objects.all()
    serializer_class = ChildSerializer
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        return Response(serializer.data)
