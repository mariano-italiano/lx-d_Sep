#!/bin/bash

sudo apt install -y ca-certificates curl gnupg lsb-release vim

for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do sudo apt-get remove $pkg; done

sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update

sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

cd /tmp
curl -s https://api.github.com/repos/goharbor/harbor/releases/latest | grep browser_download_url | cut -d '"' -f 4 | grep '\.tgz$' | wget -i -
tar -xzvf /tmp/harbor-offline-installer-v2.11.1.tgz
sudo mv harbor /opt/

cd /opt/harbor
openssl genrsa -out ca.key 2048
openssl req -new -x509 -days 365 -key ca.key -subj "/C=PL/ST=Warsaw/L=Waw/O=Lab, Inc./CN=Lab Root CA" -out ca.crt
openssl req -newkey rsa:2048 -nodes -keyout server.key -subj "/C=PL/ST=Warsaw/L=Waw/O=Lab, Inc./CN=*.lab.local" -out server.csr
openssl x509 -req -extfile <(printf "subjectAltName=DNS:registry.lab.local,DNS:www.registry.lab.local") -days 365 -in server.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out server.crt

cp harbor.yml.tmpl harbor.yml

# update certs and hostname
sed -i 's/hostname: reg.mydomain.com/hostname: registry.lab.local/' harbor.yml
sed -i 's|certificate: /your/certificate/path|certificate: /opt/harbor/server.crt|' harbor.yml
sed -i 's|private_key: /your/private/key/path|private_key: /opt/harbor/server.key|' harbor.yml

# start docker Harbor application
#./install.sh
