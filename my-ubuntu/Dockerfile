FROM ubuntu

RUN apt-get update -y \
	&& mkdir /opt/my-app \
        && apt-get install curl vim -y

COPY default.conf /tmp/my-config.conf

ENV APP_PATH="/opt/my-app"
