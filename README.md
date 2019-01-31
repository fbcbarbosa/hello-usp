# Hello USP

Código da palestra "O que raios é um Kubernete?" apresentada no USPCodeLab Summer School 2019. Testado em um sistema Ubuntu 18.

Pré-requisitos:

* Instalar Docker (https://docs.docker.com/install/linux/docker-ce/ubuntu/)
* Instalar o Minikube (https://kubernetes.io/docs/tasks/tools/install-minikube/)

### Inicializando

```bash
$ minikube start --vm-driver=kvm2
$ kubectl get nodes
$ eval $(minikube docker-env) # necessário para expor imagens Docker locais ao Minikube
```

### Build do Container Docker

```bash
$ docker build . -t hello:v1 --no-cache
$ docker run --rm -p 8080:8080 hello
```

Acesse localhost:8080 e veja o serviço rodando.

### Limitando Recursos

```bash
$ docker run --rm -p 8080:8080 --memory=256M --cpus=1 hello
$ docker stats
```

### Primeiro Deploy

```bash
$ kubectl create deployment hello --image=hello:v1
$ kubectl get pods
$ kubectl get deployments
```

Veja como o Kubernetes mantém sempre 1 deploy ativo:

```bash
$ kubectl delete pod <substituir com o nome do pod> --force --grace-period=0
```

Visualizando os recursos no Dashboard:

```bash
$ minikube dashboard
```

### Expondo um Serviço

```bash
$ kubectl expose deployment hello --type=LoadBalancer --port=8080
$ kubectl get services
$ minikube service hello --url
```

Acesse a URL e veja o serviço rodando.

### Escalando um Serviço

```bash
$ kubectl scale deployment/hello --replicas=10
$ kubectl get pods
$ minikube service hello --url
```

Acesse a URL múltiplas vezes e veja como cada requisição cai em um contêiner diferente.

### Atualizando um Serviço

Altere o código de app.py; por exemplo, altere `name = "Mundo"` por `name = "USP"`.

```bash
$ docker build . -t hello:v2
```

Atualize o deployment:

```bash
$ kubectl --record deployment/hello set image deployment/hello hello=hello:v2
```

Ou, se preferir:

```bash
$ kubectl edit deployment/hello
```

E altere `.spec.template.spec.containers[0].image` para `hello:v2`

```bash
$ kubectl get pods
```

Verifique que os pods antigos foram removidos e novos foram criados.

```bash
$ minikube service hello --url
```

Acesse a URL e verifique que a mensagem mudou.
