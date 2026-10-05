# Demo

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8080
```

Open:

- `http://localhost:8080/healthz`
- `http://localhost:8080/info`

## Run with Docker

```bash
docker build -t ai-k8s-troubleshooter:local .
docker run --rm -p 8080:8080 ai-k8s-troubleshooter:local
```

## Deploy with manifests

```bash
kubectl apply -f manifests/deployment.yaml
kubectl get pods,svc -l app=ai-k8s-troubleshooter
```

## Deploy with Helm

```bash
helm upgrade --install ai-k8s-troubleshooter ./helm/ai-k8s-troubleshooter
```
