# Kubernetes Self-Healing & Auto-Scaling Demo 🚀

A hands-on Kubernetes project demonstrating automated pod recovery, rolling updates, rollbacks, and Horizontal Pod Autoscaling (HPA).

This project demonstrates how Kubernetes maintains application availability, handles deployment updates, and automatically scales application pods based on CPU utilization.

## 🏗️ Project Structure

```text
Kubernetes-self-healing-demo/
│
├── app.py
├── Dockerfile
├── requirements.txt
│
└── kubernetes/
    ├── config.yaml
    ├── deployment.yaml
    ├── hpa.yaml
    ├── ingress.yaml
    └── service.yaml
```

## 🛠️ Technologies Used

- Docker
- Kubernetes
- YAML
- Python
- kubectl
- Horizontal Pod Autoscaler (HPA)

## ✨ Features Implemented

### 1. Self-Healing
- Kubernetes automatically recreates failed or deleted pods.
- Maintains the desired number of replicas using Deployments.
- Demonstrates automatic recovery without manual intervention.

### 2. Rolling Updates
- Updates application versions without manually deleting existing pods.
- Uses Kubernetes rolling update strategy.
- Helps maintain application availability during deployments.

### 3. Rollbacks
- Reverts deployments to a previous stable version.
- Uses Kubernetes rollout history and undo functionality.

### 4. Horizontal Pod Autoscaling (HPA)
- Automatically scales pod replicas based on CPU utilization.
- Configured a CPU utilization target of 50%.
- Demonstrates scale-out and scale-in behaviour based on resource usage.

## 📂 Kubernetes Resources

| File | Description |
|---|---|
| `deployment.yaml` | Manages application pods and replicas |
| `service.yaml` | Provides network access to pods |
| `ingress.yaml` | Manages external HTTP routing |
| `config.yaml` | Stores application configuration |
| `hpa.yaml` | Configures automatic pod scaling |

## ⚙️ Setup & Deployment

### Prerequisites

- Docker installed
- Kubernetes cluster running
- kubectl configured
- Metrics Server installed for HPA functionality

### Step 1: Clone the Repository

```bash
git clone <your-repository-url>
cd Kubernetes-self-healing-demo
```

### Step 2: Build Docker Image

```bash
docker build -t <your-image-name>:v1 .
```

Make sure the image name in `deployment.yaml` matches your built image.

### Step 3: Deploy Kubernetes Resources

```bash
kubectl apply -f kubernetes/
```

### Step 4: Verify Resources

```bash
kubectl get pods
kubectl get deployments
kubectl get services
kubectl get ingress
kubectl get hpa
```

## 🧪 Testing & Validation

### Self-Healing Test

Delete a running pod and observe Kubernetes automatically creating a replacement.

```bash
kubectl get pods
kubectl delete pod <pod-name>
kubectl get pods -w
```

### Rolling Update

Update the application image in the deployment configuration and apply the changes.

```bash
kubectl apply -f kubernetes/deployment.yaml
kubectl rollout status deployment/demo-deployment
```

### Rollback Test

```bash
kubectl rollout history deployment/demo-deployment
kubectl rollout undo deployment/demo-deployment
```

### HPA Test

Monitor automatic pod scaling:

```bash
kubectl get hpa -w
kubectl get pods -w
```

## 📚 Key Learnings

- Kubernetes Deployments and ReplicaSets
- Pod lifecycle and self-healing
- Rolling update strategies
- Deployment rollback and revision history
- Horizontal Pod Autoscaling
- CPU-based resource scaling
- Kubernetes Services and Ingress

## 👩‍💻 Author

**Samidha Wani**

GitHub: [samidha1-1](https://github.com/samidha1-1)

