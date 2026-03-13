from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from forecaster import OnyxForecaster
import uvicorn

app = FastAPI(title=\"Onyx Forecaster API\", version=\"1.0.0\")
model = OnyxForecaster()

class SalesData(BaseModel):
    date: str
    sales: float

class TrainRequest(BaseModel):
    data: List[SalesData]

@app.get(\"/\")
def read_root():
    return {\"status\": \"online\", \"service\": \"Onyx Sales Forecaster\", \"version\": \"1.0.0\"}

@app.post(\"/train\")
def train_model(payload: TrainRequest):
    try:
        data_dicts = [item.model_dump() for item in payload.data]
        model.train(data_dicts)
        return {\"message\": \"Model trained successfully\"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get(\"/forecast/{days}\")
def get_forecast(days: int):
    if not model.is_trained:
        raise HTTPException(status_code=400, detail=\"Model is not trained yet.\")
    try:
        predictions = model.forecast(days=days)
        return {\"forecast\": predictions}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == \"__main__\":
    uvicorn.run(app, host=\"0.0.0.0\", port=8000)