from fastapi import FastAPI
from src.inference.inference import Inferencer
from src.processing.preprocessing import Preprocessor
from pydantic import BaseModel

from datetime import datetime


class Features(BaseModel):
    PULocationID: int
    DOLocationID: int
    TripDistance: float
    PickupDatetime: datetime


app = FastAPI()


preprocessor = Preprocessor()
inferencer = Inferencer()


@app.get("/")
async def root():

    return {"message": "Welcome to the travel time prediction service!"}


@app.post("/predict/v1")
async def predict(features: Features):

    preprocessed_features = preprocessor.preprocess(features.dict())

    return {"message": inferencer.predict(preprocessed_features)[0],
            "features": preprocessed_features}
