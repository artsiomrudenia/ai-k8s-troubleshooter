from fastapi import FastAPI

app = FastAPI(title="ai-k8s-troubleshooter", version="0.1.0")


@app.get("/healthz")
def healthz() -> dict:
    return {"status": "ok"}


@app.get("/info")
def info() -> dict:
    return {
        "project": "ai-k8s-troubleshooter",
        "description": "AI-assisted Kubernetes troubleshooting service",
        "domain": "kubernetes",
    }
