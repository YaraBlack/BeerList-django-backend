from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BeerSerializer
from .models import Beer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

# Create your views here.


@api_view(["GET"])
def hello_world(request):
    return Response({"message": "Hello World!"})


class BeerListAll(APIView):
    """
    List all beers or create a new beer instance.
    """

    def get(self, request):
        beers = Beer.objects.all()
        serializer = BeerSerializer(beers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BeerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BeerListById(APIView):
    """
    Retrieve, update or delete a beer instance.
    """

    def get_object(self, pk):
        try:
            return Beer.objects.get(pk=pk)
        except Beer.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        beer = self.get_object(pk)
        serializer = BeerSerializer(beer)
        return Response(serializer.data)

    def put(self, request, pk):
        beer = self.get_object(pk)
        serializer = BeerSerializer(beer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        beer = self.get_object(pk)
        beer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
