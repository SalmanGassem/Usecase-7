from fastapi import FastAPI
import joblib
from pydantic import BaseModel
import numpy as np

model = joblib.load("Models/knn_model.joblib")

# Define a Pydantic model for input data validation
class InputFeatures(BaseModel):
    Appearance: float
    Minutes_played: float
    Highest_value: float

def preprocessing(input_features: InputFeatures):

    dict_f = {
    'appearance': input_features.Appearance,
    'minutes played': input_features.Minutes_played,
    'highest_value': input_features.Highest_value,
    }

    # converting the input data to a numpy array as the model expects this
    data = np.array([[dict_f["appearance"], dict_f["minutes played"], dict_f["highest_value"]]])

    return data

app = FastAPI()

# Get Predict
@app.get("/predict")
def predict(input_features: InputFeatures):
    return preprocessing(input_features)

# Post Predict
@app.post("/predict")
async def predict(input_features: InputFeatures):
    data = preprocessing(input_features)
    y_pred = model.predict(data)
    return {"pred": y_pred.tolist()[0]}

# Get request
@app.get("/")
def read_root():
    return "Welcome To Tuwaiq Academy"

# Get request
@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}

## This is just an example command to predict
# curl -X POST "http://localhost:8000/predict" -H "Content-Type: application/json" -d '{"Appearance": 23, "Minutes_played": 46, "Highest_value": 1500000}'
