from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
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

@api_view(['GET'])
def listarContato(request):
    contatos = Contato.objects.all()
    serializer = ContatoSerializer(contatos, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
def atualizarContato(request, pk):
    try:
        contato = Contato.objects.get(id = pk)
    except Contato.DoesNotExist
        return Response(status=status.HTTP_404_NOT_FOUND)