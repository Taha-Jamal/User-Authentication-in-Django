from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Note
from .serializer import NoteSerializer

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
# Create your views here.

@api_view(['GET'])
#  now u need to be authenticated to access
@permission_classes([IsAuthenticated])
def get_notes(request):
    user = request.user
    notes = Note.objects.filter(owner=user)
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)




