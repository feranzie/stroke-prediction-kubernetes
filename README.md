# stroke prediction service w kubernetes


## clone repo
```bash
git clone https://github.com/feranzie/stroke-prediction-kubernetes.git
```
# train the model
```bash
python train.py
```

## Build docker image

```bash
docker build -t stroke-prediction:v1 .       
```
## install kind and kubectl
## deploying the cluster locally
# create knd cluster
```bash
kind create cluster --name <name of cluster>     
```
## push docker container into kind cluster

```bash
kind load docker-image stroke-prediction:v1 .   
#kubectl apply -f my-manifest-using-my-image:unique-tag    
```

## apply the deployment 

```bash
kubectl aply -f deployment.yaml      
```
## apply the service   

```bash
kubectl aply -f service.yaml      
```
## get the pod id 

```bash
kubectl get pods  
```
## forward the port so you can access the cluster locally

```bash
kubectl port forward <name of pod> 8000:8000   
```