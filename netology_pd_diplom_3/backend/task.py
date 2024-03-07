import time

from celery import shared_task
from requests import get

from yaml import load as load_yaml, Loader

from backend.models import Shop, Category, Product, ProductInfo, Parameter, ProductParameter, User
from app.celery import app
from typing import Type
from django.http import JsonResponse

from django.conf import settings
from django.core.mail import EmailMultiAlternatives

from backend.models import ConfirmEmailToken, User


@shared_task
# @app.task()
def new_user_registered_send_email(email, key):
    msg = EmailMultiAlternatives(
        # title:
        f"Password Reset Token for {email}",
        # message:
        key,
        # from:
        settings.EMAIL_HOST_USER,
        # to:
        [email]
    )
    msg.send()


@shared_task
def new_order_signal(email, **kwargs):
    """
    отправяем письмо при изменении статуса заказа
    """

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
        [email]
    )
    msg.send()


@shared_task
def parsing(url, user_id):
    stream = get(url).content
    data = load_yaml(stream, Loader=Loader)
    shop, _ = Shop.objects.get_or_create(name=data['shop'], user_id=user_id)

    for category in data['categories']:
        category_object, _ = Category.objects.get_or_create(id=category['id'], name=category['name'])
        category_object.shops.add(shop.id)
        category_object.save()
    ProductInfo.objects.filter(shop_id=shop.id).delete()

    for item in data['goods']:
        product, _ = Product.objects.get_or_create(name=item['name'], category_id=item['category'])

        product_info = ProductInfo.objects.create(product_id=product.id,
                                                  external_id=item['id'],
                                                  model=item['model'],
                                                  price=item['price'],
                                                  price_rrc=item['price_rrc'],
                                                  quantity=item['quantity'],
                                                  shop_id=shop.id)

        for name, value in item['parameters'].items():
            parameter_object, _ = Parameter.objects.get_or_create(name=name)
            ProductParameter.objects.create(product_info_id=product_info.id,
                                            parameter_id=parameter_object.id,
                                            value=value)
