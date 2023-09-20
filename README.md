## Under Armour

I like Under Armour.

The purpose of this program is to scrap the brazilian Under Armour store searching for promotions.

The main code is written inside `app/app.py`.


### Requirements

* Python 3.11+
* Poetry

## How to Test It In Kubernetes
###Open the file k8s/configmap and set the environment variables for the pod

1. Be sure to have installed Minikube
```shell
minikube start
```

2. Observalility tool for k8s: https://betterstack.com/docs/logs/kubernetes/?source=360797
```shell
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/download/v0.6.4/components.yaml
```

```shell
wget -O vector-agent.toml https://logs.betterstack.com/vector-toml/kubernetes/n8v7FcsJD3VQ7qTmZofS24ME
```

```shell
kubectl apply -k k8s/logging
```

```shell
kubectl rollout restart -n vector daemonset/vector
```


3. In the root folder, set the namespace:
```shell
kubectl replace --force -f k8s/namespace.yml
```
4. Set the environment variables for the container:
```shell
kubectl replace --force -f k8s/configmap.yml
```

5. Set the CronJob
```shell
kubectl replace --force -f k8s/job.yml
```