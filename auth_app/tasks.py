import json

import requests
from django.conf import settings
from .models import SignupInfo
from celery import Celery


app = Celery()


@app.task
def save_signup_info(user_id, ip_adress):
    url = f"{settings.IP_INFO_URL}/?api_key={settings.IP_API_KEY}&ip_address={ip_adress}"
    r = requests.get(url)
    data = json.loads(r.content)
    SignupInfo.objects.create(user_id=user_id, info=data)
    return data


@app.task
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip