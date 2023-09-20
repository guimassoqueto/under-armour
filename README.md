## Under Armour

I like Under Armour.

The purpose of this program is to scrap the brazilian Under Armour store searching for promotions.

The main code is written inside `app/app.py`.


### Requirements

* Python 3.11+
* Poetry

## How to Test It In Kubernetes

* Configure The logger: https://betterstack.com/docs/logs/kubernetes/?source=360797


1. Be sure to have installed Minikube
```shell
minikube start
```
2. In the root folder, set the namespace:
```shell
kubectl replace --force -f k8s/namespace.yml
```
3. Set the environment variables for the container:
```shell
kubectl replace --force -f k8s/configmap.yml
```

5. Set the CronJob
```shell
kubectl replace --force -f k8s/job.yml
```