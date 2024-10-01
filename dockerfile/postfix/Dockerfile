# Install base image
FROM alpine:3.17

# Install dependecies
RUN apk add --no-cache \
        bash \
        vim \
        curl \
        util-linux \
        openrc \
        net-tools \
        ca-certificates \
        libsasl \
        mailx \
        postfix \
        runit \
        bind-tools \
        postfix-policyd-spf-perl

# Copy initial configuration
COPY main.cf /etc/postfix/

# Forward logs to docker log collector
RUN ln -sf /dev/stdout /var/log/postfix.log

# Expose ports
EXPOSE 25/tcp

# Startup postfix
CMD ["/usr/sbin/postfix", "start-fg"]
