from celery_tasks.rabbitmq_config import RABBITMQ_USER, RABBITMQ_PWD, RABBITMQ_HOST, RABBITMQ_PORT
import os
broker_url = f'pyamqp://{RABBITMQ_USER}:{RABBITMQ_PWD}@{RABBITMQ_HOST}:{RABBITMQ_PORT}'
result_backend = os.environ.get('CELERY_RESULT_BACKEND', 'rpc://')
