from rest_framework import serializers
from players.models import Player
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    players = serializers.PrimaryKeyRelatedField(many=True, queryset=Player.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'players']


class PlayerSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Player
        fields = ['identifier', 'name', 'last_name', 'team', 'number', 'owner', 'created_at']
