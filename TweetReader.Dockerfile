FROM python:3-stretch

WORKDIR /app

COPY server /app/server

RUN pip install --trusted-host pypi.python.org -r ./server/requirements.txt

EXPOSE 50051

CMD ["python", "./server/tweet_reader.py"]
