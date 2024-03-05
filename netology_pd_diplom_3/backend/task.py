from celery import shared_task
from requests import get

from yaml import load as load_yaml, Loader

from backend.models import Shop, Category, Product, ProductInfo, Parameter, ProductParameter, User
from app.celery import app
from typing import Type

from django.conf import settings
from django.core.mail import EmailMultiAlternatives

from backend.models import ConfirmEmailToken, User


@shared_task
# @app.task()
def new_user_registered(user_id):
    user = User.objects.get(id=user_id)
    token, _ = ConfirmEmailToken.objects.get_or_create(user_id=user.pk)

    msg = EmailMultiAlternatives(
        # title:
        f"Password Reset Token for {user.email}",
        # message:
        token.key,
        # from:
        settings.EMAIL_HOST_USER,
        # to:
        [user.email]
    )
    msg.send()


@shared_task
def new_order_signal(user_id, **kwargs):
    """
    отправяем письмо при изменении статуса заказа
    """
    # send an e-mail to the user
    user = User.objects.get(id=user_id)

    msg = "Заказ сформирован"

    if 'msg' in kwargs.keys():
        msg = kwargs['msg']

    msg = EmailMultiAlternatives(
        # title:
        f"Обновление статуса заказа",
        # message:
        msg,
        # from:
        settings.EMAIL_HOST_USER,
        # to:
        [user.email]
    )
    msg.send()
