from django.db import models

# Create your models here.
from zitalkproject import helper

class MessageThread(models.Model):
    hash_id = models.CharField(max_length=32, default=helper.create_hash, unique=True)
    title = models.CharField(max_length=64)
    clients = models.ManyToManyField('zitalkapp.User', blank=True)
    last_message = models.ForeignKey('messaging.Message', null=True, blank=True, on_delete=models.SET_NULL)

class Message(models.Model):
    hash_id = models.CharField(max_length=32, default=helper.create_hash, unique=True)
    date = models.IntegerField(default=helper.time_stamp)
    text = models.CharField(max_length=1024)
    thread = models.ForeignKey('messaging.MessageThread', on_delete = models.CASCADE, related_name='messages')
    sender = models.ForeignKey('zitalkapp.User', on_delete=models.SET_NULL,null=True)

class UnreadReceipt(models.Model):
    date = models.IntegerField(default=helper.time_stamp)