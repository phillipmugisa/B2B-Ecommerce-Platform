from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
from django.db.models import Q

import os
import uuid
import json
import datetime

# from apps
from supplier import models as SupplierModels
from auth_app import models as Authmodels


# utility functions
def get_chat_file_path(instance, chat_filename_key):
    ext = ".json"
    filename = instance.roomname
    path = os.path.join(f"{settings.CHATROOMFILES_DIRS.get(chat_filename_key)}/{filename}{ext}")
    return path

# chats and chatrooms
class Chat(models.Model):
    class Meta:
        ordering = ["-updated_on"]

    roomname = models.CharField(_("Chatroom Name"), max_length=256, unique=True, null=True, blank=True)
    chatfilepath = models.CharField(
        _("Chat filepath"),
        max_length=256,
        blank=True,
        null=True,
        unique=True
    )
    is_closed = models.BooleanField(_("Chat Closed"), default=False)
    is_handled = models.BooleanField(_("Chat handled"), default=False)
    created_on = models.DateField(_("Created on"), default=timezone.now)
    updated_on = models.DateTimeField(_("Updated on"), null=True, blank=True)

    def save(self, *args, **kwargs):
        self.chatfilepath = get_chat_file_path(self, self.chat_filename_key)
        self.updated_on = datetime.datetime.now()
            
        # try:
        #     with open(f"{self.chatfilepath}", "w") as file:
        #         json.dump([], file)
        # except FileNotFoundError:
        #     self.chatfilepath = None

        super().save(*args, **kwargs)


class SupportClientChat(Chat):
    '''
        Support -Client(Buyer/Supplier Chatroom)
    '''

    chat_filename_key = "support-client"

    user = models.ForeignKey(
        Authmodels.User,
        on_delete=models.CASCADE,
    )
    support = models.ForeignKey(
        Authmodels.SupportProfile,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

# order chat in supplier models
class InterClientChat(Chat):
    '''
        Client Chatroom
        max users: 2
    '''
    chat_filename_key = "interclient"
    initiator = models.ForeignKey(
        Authmodels.ClientProfile,
        on_delete=models.CASCADE,
        related_name="initiator"
    )
    participant = models.ForeignKey(
        Authmodels.ClientProfile,
        on_delete=models.CASCADE,
        related_name="participant"
    )

class InterUserChat(Chat):
    '''
        Client Chatroom
        max users: 2
    '''
    chat_filename_key = "interuser"
    participants = models.ManyToManyField(to=Authmodels.User, related_name="chat_participants", blank=True)

class GroupChat(Chat):
    '''
        Client Chatroom
        max users: 2
    '''
    chat_filename_key = "groupchat"
    name = models.CharField(_("Chatroom Name"), max_length=256, null=True, blank=True)
    image = models.ImageField(
        verbose_name=_("Image"),
        upload_to=Authmodels.get_file_path,
        blank=True,
        null=True,
        default="assets/imgs/resources/profiledefault.png",
    )
    participants = models.ManyToManyField(to=Authmodels.User, related_name="group_participants", blank=True)

class OrderChat(Chat):
    '''
        Order Chatroom
    '''
    chat_filename_key = "orders"
    order = models.OneToOneField(to=SupplierModels.Order, on_delete=models.CASCADE)
    
    buyer_representative = models.ForeignKey(
        Authmodels.User,
        on_delete=models.CASCADE,
        related_name="buyer_user",
        blank=True,
        null=True,
    )
    supplier_representative = models.ForeignKey(
        Authmodels.User,
        on_delete=models.CASCADE,
        related_name="supplier_user",
        blank=True,
        null=True,
    )

    def save(self, *args, **kwargs):
        if not self.roomname:
            self.roomname = self.order.order_id
        super().save(*args, **kwargs)
