FROM ubuntu
MAINTAINER altkom 
RUN apt-get update && apt-get install -y apache2
COPY index.html /var/www/html/
CMD ["apachectl", "-D", "FOREGROUND"]
EXPOSE 80
