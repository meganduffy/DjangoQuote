from __future__ import unicode_literals

from django.db import models


class Quote(models.Model):

    class Meta:
        app_label = "DjangoQuote_app"

    # Field definitions
    author = models.CharField(max_length=255)
    quote = models.CharField(max_length=500)

    def __str__(self):
        return '- '.join([self.author,
                        self.quote])
