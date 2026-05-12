# Argo MLOps: Демонстрационный конвейер обучения моделей

Данный проект представляет собой пример реализации MLOps-пайплайна с использованием **Argo Workflows** и **Argo CD** в кластере Kubernetes. Проект автоматизирует процесс генерации синтетических данных, обучения модели машинного обучения и валидации результатов.

## 🚀 Обзор архитектуры

Проект построен по принципу GitOps и разделен на следующие этапы:

1.  **Подготовка данных**: Генерация синтетического набора логов (информационные сообщения vs ошибки).
2.  **Обучение**: Обучение модели логистической регрессии с использованием TF-IDF векторизации.
3.  **Оркестрация**: Управление шагами через DAG (Directed Acyclic Graph) в Argo Workflows.
4.  **Хранение**: Использование Persistent Volume Claim (PVC) для передачи данных и модели между шагами пайплайна.

## 🛠 Технологический стек

- **Язык**: Python 3
- **ML Библиотеки**: `scikit-learn`, `pandas`, `joblib`
- **Оркестрация**: Argo Workflows
- **CD**: Argo CD
- **Инфраструктура**: Kubernetes, Docker, Helm

## 📋 Описание компонентов

### 1. Конвейер обработки (Pipeline)
Пайплайн определен в `k8s/argo-pipeline.yaml` и состоит из трех последовательных шагов:
- `generate-data`: Запускает `generate_data.py`, создавая файл `dataset.csv`.
- `train-model`: Запускает `train.py`, который считывает данные, обучает модель и сохраняет `model.joblib`.
- `validate-metrics`: Проверяет содержимое рабочей директории (в данной демо-версии выполняет команду `ls -R`).

### 2. ML Модель
- **Задача**: Бинарная классификация текстовых логов (INFO vs ERROR).
- **Метод**: TF-IDF Vectorizer $\rightarrow$ Logistic Regression.
- **Результат**: Сохраненный артефакт модели в формате `.joblib`.

### 3. Инфраструктурный слой
- **Dockerfile.train**: Образ, содержащий все необходимые зависимости для выполнения всех этапов пайплайна.
- **PVC (Persistent Volume Claim)**: Обеспечивает общую файловую систему (`/app/data`) для всех контейнеров в рамках одного Workflow.
- **Argo App**: Конфигурация для автоматического развертывания ресурсов через Argo CD.

## ⚙️ Инструкция по запуску

### Шаг 1: Сборка образа
```bash
docker build -t ml-pipeline-train:v3 -f Dockerfile.train .
```

### Шаг 2: Настройка инфраструктуры и K8s
```bash
# 1. Установка Argo Workflows через Helm
curl -L -o argo-workflows.tgz https://github.com/argoproj/argo-helm/releases/download/argo-workflows-1.0.13/argo-workflows-1.0.13.tgz
helm install argo argo-workflows.tgz --namespace argo --create-namespace --set server.authMode=server

# 2. Создание общего тома для данных
kubectl apply -f k8s/pvc-argo.yaml

# 3. Развертывание через Argo CD
kubectl apply -f k8s/argo-app.yaml
```

### Шаг 3: Запуск обучения
```bash
# Через Argo CLI
argo submit -n argo -f k8s/argo-pipeline.yaml

# Или через kubectl
kubectl apply -f k8s/argo-pipeline.yaml
```

## 📁 Структура проекта
- `src/`: Исходный код (генерация, обучение, UI).
- `k8s/`: Манифесты Kubernetes и определения Workflow.
- `data/`: Локальное хранилище данных (используется при локальном запуске).
- `Dockerfile.train`: Рецепт сборки среды выполнения.
