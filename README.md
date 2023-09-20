## Under Armour

I like Under Armour.

The purpose of this program is to scrap the brazilian Under Armour store searching for promotions.

The main code is written inside `app/app.py`.


### Requirements

* Python 3.11+
* Poetry

## How to Test It In Kubernetes

* Configure The logger: https://betterstack.com/docs/logs/kubernetes/?source=360797

```shell
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/download/v0.6.4/components.yaml
```

```shell
wget -O vector-agent.toml https://logs.betterstack.com/vector-toml/kubernetes/n8v7FcsJD3VQ7qTmZofS24ME
```


1. Be sure to have installed Minikube
```shell
minikube start
```
1. In the root folder, set the namespace:
```shell
kubectl replace --force -f k8s/namespace.yml
```
1. Set the environment variables for the container:
```shell
kubectl replace --force -f k8s/configmap.yml
```

1. Set the CronJob
```shell
kubectl replace --force -f k8s/job.yml
```