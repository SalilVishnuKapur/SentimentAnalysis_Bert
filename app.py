from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

app = FastAPI()

class InputText(BaseModel):
    text: str

tokens = AutoTokenizer.from_pretrained("nlptown/bert-base-multilingual-uncased-sentiment")
model = AutoModelForSequenceClassification.from_pretrained("nlptown/bert-base-multilingual-uncased-sentiment")

@app.post("/predict")
async def predict_sentiment(review: InputText):
    tokens_text = tokens(review, return_tensors='pt', truncation=True, padding=True)
    out = model(**tokens_text)
    scores = torch.nn.functional.softmax(out.logits, dim=1)
    predicted_label = torch.argmax(scores, dim=1).item()
    return {"sentiment_label": int(predicted_label)}