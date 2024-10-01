FROM nginx:1.19.2

# Overwrite default config of nginx with my custom config including Basic Auth for web server
COPY default.conf /etc/nginx/conf.d/default.conf

# Copy credential file into nginx config
COPY .htpasswd /etc/nginx/conf.d/.htpasswd

