import uuid

from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    team = models.CharField(max_length=100, blank=False)
    number = models.IntegerField(blank=False)
    owner = models.ForeignKey('auth.User', related_name='players', on_delete=models.CASCADE)
    identifier = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']

    def save(self, *args, **kwargs):
        self.identifier = uuid.uuid1()
        super(Player, self).save(*args, **kwargs)
