FROM python:3.8
ADD ./producerFastApi/requirements.txt /
ADD ./producerFastApi/main.py /
ADD ./celery_tasks/ /celery_tasks/
RUN pip3 install -r requirements.txt
ENTRYPOINT uvicorn main:app --host 0.0.0.0 --port 5001