from django.contrib.auth.models import User, Group
from rest_framework import serializers
#  que campos vamos a volcar en la api

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

# ejemplo de como lo haremos

class MyModel:
    def __init__(self, name, description, number):
        self.name = name
        self.description = description
        self.number = number

json = """
{
    "name": "foo",
    "description": "bar",
    "number": 123
}
"""