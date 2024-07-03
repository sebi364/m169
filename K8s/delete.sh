#!/usr/bin/bash
kubectl delete -f ingress.yml
kubectl delete -f webapp.yml
kubectl delete -f database.yml
kubectl delete -f shared-configs.yml
kubectl delete -f shared-secrets.yml