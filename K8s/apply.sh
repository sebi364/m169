#!/usr/bin/bash
kubectl apply -f shared-secrets.yml
kubectl apply -f shared-configs.yml
kubectl apply -f mariadb-init-config.yml
kubectl apply -f database.yml
kubectl apply -f webapp.yml
kubectl apply -f ingress.yml