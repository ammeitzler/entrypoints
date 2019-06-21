from django.contrib.auth.models import User, Group
from rest_framework import serializers
from api.models import *



class AnticipatingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Anticipating
        fields = ('question',)

class CheckSentimentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CheckSentiment
        fields = ('question',)

class CheckSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Check
        fields = ('question',)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')