FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirement.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirement.txt
COPY . /code/
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh