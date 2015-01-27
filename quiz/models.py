from django.db import models
from django.conf import settings


class Answer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    value = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.value
