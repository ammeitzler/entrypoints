from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from api.serializers import *
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse



class AnticipatingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Anticipating.objects.all()
    serializer_class = AnticipatingSerializer
    def list(self, request):
    	queryset = Anticipating.objects.all()
    	serializer = AnticipatingSerializer(queryset, context={'request': None}, many=True)
    	return JsonResponse(serializer.data, json_dumps_params={'indent': 2}, safe=False)

class CheckSentimentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = CheckSentiment.objects.all()
    serializer_class = CheckSentimentSerializer
    def list(self, request):
    	queryset = CheckSentiment.objects.all()
    	serializer = CheckSentimentSerializer(queryset, context={'request': None}, many=True)
    	return JsonResponse(serializer.data, json_dumps_params={'indent': 2}, safe=False)

class CheckViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Check.objects.all()
    serializer_class = CheckSerializer
    def list(self, request):
    	queryset = Check.objects.all()
    	serializer = CheckSerializer(queryset, context={'request': None}, many=True)
    	return JsonResponse(serializer.data, json_dumps_params={'indent': 2}, safe=False)

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer