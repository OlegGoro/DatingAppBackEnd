from django.contrib import admin
from .models import Claims
from .models import Messages
from .models import ChatSession

admin.site.register(Claims)
admin.site.register(Messages)
admin.site.register(ChatSession)
