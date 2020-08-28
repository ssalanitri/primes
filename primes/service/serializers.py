from django.contrib.auth.models import User, Group
from rest_framework import serializers
import primes.plist 


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class PlistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Plist
        fields = ['url', 'name']