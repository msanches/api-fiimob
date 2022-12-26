FROM alpine
EXPOSE 80
RUN apk add py3-pip

COPY . /opt/app
RUN pip3 install -r /opt/app/requirements.txt
WORKDIR /opt/app
CMD flask run --host 0.0.0.0