from fastapi import FastAPI
from app.schemas.input import InputText
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

app = FastAPI()

tokens = AutoTokenizer.from_pretrained("nlptown/bert-base-multilingual-uncased-sentiment")
model = AutoModelForSequenceClassification.from_pretrained("nlptown/bert-base-multilingual-uncased-sentiment")

@app.post("/predict")
def predict_sentiment(review: InputText):
    tokens_text = tokens(review.text, return_tensors='pt', truncation=True, padding=True)
    out = model(**tokens_text)
    scores = torch.nn.functional.softmax(out.logits, dim=1)
    predicted_label = torch.argmax(scores, dim=1).item()
    return {"sentiment_label": int(predicted_label)}