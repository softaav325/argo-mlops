# Link latest version:
curl -L -o argo-workflows.tgz https://github.com/argoproj/argo-helm/releases/download/argo-workflows-1.0.13/argo-workflows-1.0.13.tgz


# Install: 
helm install argo argo-workflows.tgz --namespace argo --create-namespace  --set server.authMode=server 

#  For UI run:  
kubectl port-forward svc/argo-workflows-server -n argo 2746:2746

# Open web: 
https://localhost:2746

---

## Деплой и запуск проекта

### 1. Сборка образа для обучения
```bash
docker build -t ml-pipeline-train:v3 -f Dockerfile.train .
```

### 2. Подготовка инфраструктуры (Kubernetes)
Создание общего тома для данных:
```bash
kubectl apply -f k8s/pvc-argo.yaml
```

Развертывание приложения через Argo CD (GitOps):
```bash
kubectl apply -f k8s/argo-app.yaml
```

### 3. Запуск ML-пайплайна
Для запуска процесса генерации данных и обучения модели:
```bash
# С помощью argo CLI:
argo submit -n argo -f k8s/argo-pipeline.yaml

# Или через kubectl:
kubectl apply -f k8s/argo-pipeline.yaml
```
