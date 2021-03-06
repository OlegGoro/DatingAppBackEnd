from django.db import models
from django.utils.translation import gettext as _

class Claims(models.Model):
    name = models.CharField(max_length=255, null=False, blank=True)
    iam = models.CharField(max_length=255, null=False, blank=True)
    goal = models.CharField(max_length=255, null=False, blank=True)
    lookfor = models.CharField(max_length=255, null=False, blank=True)
    lat = models.FloatField(_('Latitude'), null=True, blank=True)
    lon = models.FloatField(_('Longitude'), null=True, blank=True)
    esttime = models.FloatField(_('Seconds'), null=True, blank=True)
    wholikes = models.CharField(max_length=255, null=False, blank=True)
    image = models.ImageField(upload_to="api/static/media/", null=True, blank=True)

    def __str__(self):
        return "{} - {}".format(self.name, self.goal, self.iam, self.lookfor, self.lat, self.lon, self.esttime, self.wholikes)

class ChatSession(models.Model):
    chatsession = models.AutoField(primary_key=True)
    esttime = models.FloatField(_('Seconds'), null=True, blank=True)
    user1 = models.CharField(max_length=255, null=False, blank=True)
    user2 = models.CharField(max_length=255, null=False, blank=True)

class Messages(models.Model):
    message = models.CharField(max_length=255, null=False)
    sender = models.CharField(max_length=255, null=False)
    receiver = models.CharField(max_length=255, null=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    chatsession = models.ForeignKey('ChatSession', related_name='messages', on_delete=models.CASCADE)
