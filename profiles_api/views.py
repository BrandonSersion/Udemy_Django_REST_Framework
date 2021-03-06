from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets

from .serializers import HelloSerializer, UserProfileSerializer
from .models import UserProfile

# Create your views here.


class HelloApiView(APIView):
    """Test API View."""

    serializer_class = HelloSerializer
    
    def get(self, request, format=None):
        """Returns a list of APIView features."""

        an_apiview = [
            'Uses HTTP methods as a function (get, post, patch, put, delete)',
            'It is similar to the traditional Django view',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with our name."""

        serializer = HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk=None):
        """Handles updating an object."""

        return Response({'method': 'put'})

    def patch(self, request, pk=None):
        """Patch request, only update fields provided in the request."""

        return Response({'method', 'patch'})

    def delete(self, request, pk=None):
        """Deletes an object."""

        return Response({'method': 'delete'})


class HelloViewset(viewsets.ViewSet):
    """Test API ViewSet."""

    def list(self, request):
        """Return a hello message."""
        
        a_viewset = [
            'Uses actions (list, create, retrieve, udate, partial_update)',
            'Automatically maps URLs to routers',
            'Provides more functionality with less code.',
        ]

        return Response({'message': 'Hello', 'a_viewset': a_viewset})

    serializer_class = HelloSerializer
    
    def create(self, request):
        """Create a new hello message."""

        serializer = HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = f'Hello {name}'
            return Response({'message', message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def retrieve(self, request, pk=None):
        """Handles getting an object by its ID."""

        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handles updating of an object."""

        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handles updating part of an object."""

        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handles removing an object."""

        return Response({'http_method', 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profiles."""

    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()