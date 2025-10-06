# SentimentAnalysis_Bert

**SentimentAnalysis_Bert** is a FastAPI-based API for **sentiment analysis** using a pre-trained BERT model (`nlptown/bert-base-multilingual-uncased-sentiment`) from HuggingFace. It provides a `/predict` endpoint to classify text into sentiment labels (0–5).

---

## Features

* FastAPI backend for RESTful API
* Pre-trained BERT model for multi-language sentiment classification
* Dockerized for easy deployment
* Simple modular structure for scalability

---

## Folder Structure

```
SentimentAnalysis_Bert/
├── app/
│   ├── service/
│   │   └── api.py          # FastAPI /predict endpoint
│   └── schemas/
│       └── input.py        # Pydantic request model
├── tests/
│   └── test_api.py         # API tests using TestClient
├── requirements.txt
├── Dockerfile
└── README.txt
```

---

## Installation

### Prerequisites

* Python 3.9+
* Docker (Only for containerized deployment)

### Local Setup

1. Clone the repository:

```powershell
git clone https://github.com/SalilVishnuKapur/SentimentAnalysis_Bert.git
cd "C:\Users\YourUserName\source\repos\SentimentAnalysis_Bert"
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Run the API:

```powershell
uvicorn app.service.api:app --host 0.0.0.0 --port 8000 --reload
```

> Note: `app.service.api:app` points to `api.py` inside `app/service/`.

---

## Docker Setup

1. Build the Docker image:

```powershell
docker build -t sentiment-bert .
```

2. Run the container:

```powershell
docker run -d -p 8000:8000 --name sentiment-bert-container sentiment-bert
```

3. Access the API at: [http://localhost:8000](http://localhost:8000)

---

## Testing

Run unit/integration tests with `pytest`:

```powershell
cd "C:\Users\YourUserName\source\repos\SentimentAnalysis_Bert"
pytest -v .\tests\test_api.py
```

* Ensure each folder has an `__init__.py` to mark it as a package:

```
app/__init__.py
app/service/__init__.py
app/schemas/__init__.py
```

* If import issues occur due to spaces in the path, set the `PYTHONPATH`:

```powershell
$env:PYTHONPATH = "C:\Users\YourUserName\source\repos\SentimentAnalysis_Bert"
pytest -v .\tests\test_api.py
```

---

## API Usage

### Endpoint

**POST** `/predict`

**Request Body**

```json
{
  "text": "I love this product!"
}
```

**Response**

```json
{
  "sentiment_label": 4
}
```

> Labels typically range from 0 (very negative) to 5 (very positive).

### Testing API with Postman

1. Open Postman and create a new **POST request**.
2. Set the request URL to:

```
http://localhost:8000/predict
```

3. Go to the **Body** tab → select **raw** → **JSON**.
4. Paste your request JSON, for example:

```json
{
  "text": "This is an amazing product!"
}
```

5. Click **Send**.
6. You should receive a JSON response with the predicted sentiment label:

```json
{
  "sentiment_label": 4
}
```

> Make sure your Docker container is running and mapped to port 8000 before sending the request.

---

## Requirements

Key Python packages:

* fastapi
* uvicorn
* transformers
* torch
* pydantic
* pytest
* requests

---

## Notes

* Model is loaded once at startup for performance.
* For development, you can mount the `app/` folder into Docker for live changes.
* Add more endpoints or services by following the current `app/service` and `app/schemas` structure.
