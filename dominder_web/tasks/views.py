from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Tarea
from .serializers import TareaSerializer

# Obtener todas las tareas
class TareaList(APIView):
    def get(self, request):
        tasks = Tarea.objects.all()
        serializer = TareaSerializer(tasks, many=True)
        return Response(serializer.data)

# Crear una nueva tarea
class TareaCreate(APIView):
    def post(self, request):
        serializer = TareaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Actualizar una tarea existente (marcar como completada)
class TareaUpdate(APIView):
    def put(self, request, pk):
        task = Tarea.objects.get(pk=pk)
        serializer = TareaSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Eliminar una tarea
class TareaDelete(APIView):
    def delete(self, request, pk):
        task = Tarea.objects.get(pk=pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
