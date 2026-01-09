from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "High-Cardinality Prediction Service is Running"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/predict")
def predict(data: dict):
    return {"prediction": "dummy_result", "input": data}