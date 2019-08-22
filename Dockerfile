FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY dependencies /code/
RUN pip install -r dependencies
COPY . /code/