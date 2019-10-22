# docker_kubernetes
Meetup demo about docker and kubernetes


## Docker

### Architecture VM vs. Docker

https://uploads.toptal.io/blog/image/91505/toptal-blog-image-1438607369520-110213f5682347c7ea0c68d46bb17d6d.jpg

### DockerHUb and images

https://hub.docker.com

$ docker login --help

$ docker pull alpine

$ docker images

$ docker run -it alpine sh

$ docker ps

$ docker system prune

$ docker rm $CONTAINERID

$ docker rmi $IMAGE -f


### Dockerfile, docker-compose and images creation  

Show dockerfiles in projects

$ docker build -t api-rest:local ..

$ docker run -p 5001:5000 fake-api:local

$ docker logs $CONTAINERID

$ docker-compose build

$ docker-compose up

$ docker-compose down


## MiniKube

### Architecture

https://blog.anant.us/wp-content/uploads/2019/02/SM.Global.Data_.Analytics.Platform.Diagram.Kubernetes.Architecture.png

### MiniKube

$ minikube status

$ minikube start

$ cat ~/.kube/config

$ kubectl get namespaces

$ kubectl get services --all-namespaces

$ kubectl get pods --all-namespaces

$ k9s

$ eval $(minikube docker-env)

$ kubectl create namespace meetup

$ kubectl create deployment nginx --image=nginx -n meetup

$ kubectl delete deployment nginx -n meetup


## Helm

- all templates are deployments
- chartmusseum

$ helm init --wait
$ helm ls
$ helm create project_name
$ helm delete --purge $DEPLOYMENTID
$ helm upgrade snug-kudu mongodb/helm/mongodb
