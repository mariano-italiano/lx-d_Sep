# Base Image from alpine defined as 'helper-clone'
FROM alpine AS helper-clone
# Install git binary
RUN apk add git
# Set workdir path
WORKDIR /src
# Define arg variable for branch name
ARG NGINX_BRANCH_NAME=1.0
# Clone github repo based on branch name
RUN git clone https://github.com/mariano-italiano/docker.git && cd docker/html && git checkout $NGINX_BRANCH_NAME 


# Base Imgage from nginx v1.19.2
FROM nginx:1.19.2
# Set author
#MAINTAINER Marcin Kujawski version 1.0
LABEL "Author"="Marcin Kujawski"
LABEL "Version"="1.0"
# Update container repo and install vim, curl
RUN apt-get update && apt-get install -y vim curl && apt-get clean 
# Copy from my 'helper-clone' image the content of the website
COPY --from=helper-clone /src/docker/html/index.html /usr/share/nginx/html/index.html

