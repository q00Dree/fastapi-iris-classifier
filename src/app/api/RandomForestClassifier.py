from pandas.core.algorithms import mode
import uvicorn
from fastapi import APIRouter, HTTPException
from src.app.api.RandomForestClassifierModel import IrisModel, IrisSpecies

RandomForestClassifier = APIRouter()
model = IrisModel()

@RandomForestClassifier.post('/predict')
def predict_species(iris: IrisSpecies):
    data = iris.dict()
    prediction, probability = model.predict_species(data['sepal_length'],
                                                    data['sepal_width'],
                                                    data['petal_length'],
                                                    data['petal_width'])
    return {'prediction': prediction, 'probability': probability}