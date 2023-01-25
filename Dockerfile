FROM python:3.8-buster
LABEL maintainer="magz3116@gmail.com"
COPY . /app
WORKDIR /app
CMD ["bash","./run.sh"]