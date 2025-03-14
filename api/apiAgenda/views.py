from django.shortcuts import render
from rest_framework import status
from .models import Contato
from .serializers import ContatoSerializer

#Criar Endpoints
@api_view(['POST'])
def inserirContato(request):
    serializer = ContatoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)
