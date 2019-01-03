from rest_framework import generics
from music.models import Claims
from music.models import Messages
from music.models import ChatSession
from music.serializers import ClaimsSerializer
from music.serializers import MessagesSerializer
from music.serializers import ChatSessionSerializer
import json
from url_filter.integrations.drf import DjangoFilterBackend
from django.db.models import Count, F, Value
from django.http import QueryDict
from django.http import HttpResponse
from django.db.models.functions import Concat
from django.utils.translation import gettext as _


class ClaimsView(generics.ListAPIView):
    queryset = Claims.objects.all()
    serializer_class = ClaimsSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['hobbies']

class PostExample(generics.ListCreateAPIView):
    serializer_class = ClaimsSerializer

class MessagesView(generics.ListAPIView):
    queryset = Messages.objects.all()
    serializer_class = MessagesSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['sender','receiver']

class AddMessageView(generics.ListCreateAPIView):
    serializer_class = MessagesSerializer

class AddChatSessionView(generics.ListCreateAPIView):
    serializer_class = ChatSessionSerializer

class ChatSessionView(generics.ListAPIView):
    queryset = ChatSession.objects.all()
    serializer_class = ChatSessionSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['users']

class AddLikeView(generics.UpdateAPIView):
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, *kwargs)

    def put(self, request, *args, **kwargs):
        data = request.data
        datadumb = json.dumps(data)
        dataparsed = json.loads(datadumb)
        User1 = Claims.objects.all().get(name=dataparsed['ClaimName'])
        User2 = Claims.objects.all().get(name=dataparsed['MyName'])
        User1Likes = getattr(User1, 'wholikes')
        User2Likes = getattr(User2, 'wholikes')
        MatchedGroup = dataparsed['ClaimName'] + " " + dataparsed['MyName']
        if (dataparsed['MyName'] not in User1Likes):
            readytoupdate = Claims.objects.all().filter(name=dataparsed['ClaimName'])
            readytoupdate.update(wholikes=Concat("wholikes", Value(" "), Value(dataparsed['MyName'])))
        if (dataparsed['MyName'] in User1Likes and dataparsed['ClaimName'] in User2Likes):
            check = "Great! Matched!"
            ChatSession.objects.create(esttime="300", users=MatchedGroup)
        else:
            check = "Sorry. No match."

        return HttpResponse(check)
