```docker run -p 127.0.0.1:16379:6379 --name redis-celery -d redis```

```-p 127.0.0.1:16379:6379:``` 127.0.0.1 - ip, ```16379:6379``` - указываем порт и пересылку, тут нам важен только первый порт - это порт контейнера


в файле setting.py есть ```CELERY_BROKER_URL = 'redis://localhost:16379/0'```, сюда нужно будет вставить свою ссылку на redis

запуск селери ```celery -A netology_pd_diplom_3 worker -l info```