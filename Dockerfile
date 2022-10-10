# TODO: 补充Dockerfile
FROM python:3.8

RUN mkdir /app
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple