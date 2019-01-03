from rest_framework import serializers
from music.models import Claims
from music.models import Messages
from music.models import ChatSession


class ClaimsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Claims
        fields = ("name", "goal", "hobbies", "lat", "lon", "esttime", "wholikes")

class MessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messages
        fields = ("message", "sender", "receiver", "timestamp", "chatsession")

class ChatSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatSession
        fields = ("chatsession", "esttime", "users")
