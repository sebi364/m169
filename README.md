# m169 - Services mit Containern bereitstellen
[![Build and Push database](https://github.com/sebi364/m169/actions/workflows/build-database.yml/badge.svg)](https://github.com/sebi364/m169/actions/workflows/build-database.yml)
[![Build and Push webapp](https://github.com/sebi364/m169/actions/workflows/build-webapp.yml/badge.svg)](https://github.com/sebi364/m169/actions/workflows/build-webapp.yml)

This repository contains the sourcefiles and container-images for our m169 project.

## Tl:Dr;

We developed a simple Flask app that serves random quotes in form of a simple JSON API. With routes for quotes, health, and UUIDs. The app uses a MariaDB database running in a Docker container. We automated the CI/CD pipeline with GitHub Actions. The K3s cluster is hosted on Proxmox and configured using Terraform. Data storage is managed with Longhorn to ensure replication and persistence.

## Deployment
This project can be deployed to an existing K3s cluster using the following commands:
```bash
git clone https://github.com/sebi364/m169
cd ./m169/K8s
kubectl apply -f .
```
Please note that some changes to the [ingress route](./K8s/ingress.yml) might be necessary, for the application to work correctly.

## Links:
* **Quotes Dataset:** https://www.kaggle.com/datasets/manann/quotes-500k
* **K3s Cluster setup:** https://www.rootisgod.com/2024/Running-an-HA-3-Node-K3S-Cluster/
* **Documentation for this project:** https://docs.google.com/document/d/1NGyn6Wito3yDE-4d_aPTKCUPobqt6S5PwaexumE2dk4/edit?usp=sharing
