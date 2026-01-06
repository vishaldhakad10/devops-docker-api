from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "DevOps Docker API running successfully"}

@app.get("/health")
def health():
    return {"status": "OK"}
