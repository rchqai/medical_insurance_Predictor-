from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import pandas as pd
import numpy as np

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API is working!"}

# Model load
with open("xgb_model.pkl", "rb") as file:
    model = pickle.load(file)

class InsuranceInput(BaseModel):
    age: int
    bmi: float
    children: int
    sex: str
    smoker: str
    region: str

@app.post("/predict")
def predict(data: InsuranceInput):
    input_data = pd.DataFrame([data.dict()])
    prediction = model.predict(input_data.to_numpy())[0]
    return {"predicted_cost": float(prediction)}