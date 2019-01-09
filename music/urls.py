from django.conf.urls import url
from django.urls import path
from .views import ClaimsView
from .views import PostExample
from .views import MessagesView
from .views import AddMessageView
from .views import AddChatSessionView
from .views import ChatSessionView
from .views import AddLikeView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('claims/', ClaimsView.as_view(), name="claims-all"),
    path('addclaim/', PostExample.as_view(), name="claims-all"),
    path('messages/', MessagesView.as_view(), name="claims-all"),
    path('addmessage/', AddMessageView.as_view(), name="claims-all"),
    path('addsession/', AddChatSessionView.as_view(), name="claims-all"),
    path('chatsessions/', ChatSessionView.as_view(), name="claims-all"),
    path('addlike/', AddLikeView.as_view(), name="claims-all"),
]
