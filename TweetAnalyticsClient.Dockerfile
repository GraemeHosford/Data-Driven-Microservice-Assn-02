FROM python:3-stretch

WORKDIR /app

COPY client /app/client

RUN pip install --trusted-host pypi.python.org -r ./client/requirements.txt

EXPOSE 50052

CMD ["python", "./client/tweet_analytics_client.py"]
