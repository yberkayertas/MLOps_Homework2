from fastapi import FastAPI
import hashlib


app = FastAPI()


@app.get("/")
def read_root():
    return {"status": "High-Cardinality Prediction Service is Running"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.get("/predict")
def predict(input_string: str):
    # Basit bir hashing logic örneği
    hash_idx = int(hashlib.md5(input_string.encode()).hexdigest(), 16) % 1000
    return {"input": input_string, "hash_index": hash_idx}

