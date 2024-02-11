#!/bin/sh

mkdir cert
openssl req -newkey rsa:4096 \
            -x509 \
            -sha256 \
            -days 3650 \
            -nodes \
            -out cert/ssl_cert.crt \
            -keyout cert/ssl_key.key \
            -subj "/C=NL/ST=Amsterdam/L=Amsterdam/O=AntiRKN/OU=IT Department/CN=www.example.com"

docker-compose build
