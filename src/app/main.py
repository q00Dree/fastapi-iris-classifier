from fastapi import FastAPI
from src.app.api.RandomForestClassifier import RandomForestClassifier

app = FastAPI()

app.include_router(RandomForestClassifier, prefix='/api/v1/rfc', tags=['rfc'])