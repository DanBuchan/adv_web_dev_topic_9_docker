from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import *
from .serializers import *

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import mixins


# @api_view(['GET', 'PUT', 'POST', 'DELETE'])
# def gene_detail(request, pk):
#
#     if request.method == 'POST':
#         serializer = GeneSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     try:
#         gene = Gene.objects.get(pk=pk)
#     except Gene.DoesNotExist:
#         return HttpResponse(status=404)
#     if request.method == 'GET':
#         serializer = GeneSerializer(gene)
#         return Response(serializer.data)
#     elif request.method == 'DELETE':
#         gene.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#     elif request.method == 'PUT':
#         serializer = GeneSerializer(gene, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GeneDetail(mixins.CreateModelMixin,
                 mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin,
                 generics.GenericAPIView):
    queryset = Gene.objects.all()
    serializer_class = GeneSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

# @api_view(['GET'])
# def genes_list(request):
#     if request.method == 'GET':
#         gene = Gene.objects.all()
#         serializer = GeneListSerializer(gene, many=True)
#         return Response(serializer.data)

class GeneList(generics.ListAPIView):
    queryset = Gene.objects.all()
    serializer_class = GeneListSerializer
