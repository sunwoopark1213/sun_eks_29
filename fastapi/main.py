from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "FastAPI + Nginx Proxy OK!"}

@app.get("/api/health")
def health():
    return {"status": "healthy"}
