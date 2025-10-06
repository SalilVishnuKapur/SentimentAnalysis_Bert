import pytest
from fastapi.testclient import TestClient
from app.service import api

client = TestClient(api.app)

def test_predict_sentiment_positive():
    """
    Test the /predict endpoint with a positive sentiment input.
    """
    payload = {"text": "I love this product!"}
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "sentiment_label" in data
    assert isinstance(data["sentiment_label"], int)
    # Optional: check predicted label is within expected range
    assert 0 <= data["sentiment_label"] <= 5  # BERT model labels usually 0-5

def test_predict_sentiment_negative():
    """
    Test the /predict endpoint with a negative sentiment input.
    """
    payload = {"text": "This is terrible and I hate it."}
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "sentiment_label" in data
    assert isinstance(data["sentiment_label"], int)
    assert 0 <= data["sentiment_label"] <= 5

def test_predict_sentiment_empty():
    """
    Test the /predict endpoint with an empty string.
    """
    payload = {"text": ""}
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "sentiment_label" in data
    assert isinstance(data["sentiment_label"], int)
