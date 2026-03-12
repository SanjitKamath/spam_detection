from fastapi import FastAPI
from pydantic import BaseModel

from src.predictor import predict_spam

app = FastAPI(title="Spam Guard API")


class Message(BaseModel):
    text: str


@app.post("/scan")

def scan(message: Message):

    result = predict_spam(message.text)

    return result