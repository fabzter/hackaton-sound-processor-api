FROM ubuntu:latest

RUN apt-get update -y && \
    apt-get install -y python-pip && apt-get install python3.7

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]