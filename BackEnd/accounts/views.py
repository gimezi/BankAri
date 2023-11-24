from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProfileSerializer
from .models import User
from django.http import JsonResponse

# Create your views here.
@api_view(['GET'])
def profile(request, username):
    serializer = ProfileSerializer(get_object_or_404(User, username = username))
    return Response(serializer.data)


@api_view(['GET'])
def check_username(request, username):
    if username:
        exist = User.objects.filter(username=username).exists()
        if exist:
            return JsonResponse({'message': '존재하는 아이디입니다.'})
    return JsonResponse({'message': '사용가능한 아이디입니다.'})