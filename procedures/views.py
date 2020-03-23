from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.response import Response

from .models import Hospital, Procedure
from .serializers import (HospitalListSerializer, HospitalSerializer,
                          ProcedureSerializer)

# Create your views here.


class HospitalView(viewsets.ModelViewSet):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer

    def list(self, request: Request, *args, **kwargs):
        queryset = Hospital.objects.all()
        serializer = HospitalListSerializer(queryset, many=True)
        return Response(serializer.data)


class ProcedureView(viewsets.ModelViewSet):
    queryset = Procedure.objects.all()
    serializer_class = ProcedureSerializer
