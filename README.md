# Smart Tourist Safety Monitoring & Incident Response System

## Features

- Blockchain-based Tourist ID
- AI anomaly detection
- Geo-fencing alerts
- Panic/SOS system
- Real-time tracking
- Police dashboard
- MongoDB integration
- Docker support

## Installation

```bash
git clone <repo-url>
cd smart-tourist-safety-system
```

## Create Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run MongoDB

```bash
docker run -d -p 27017:27017 mongo
```

## Run Backend

```bash
uvicorn app.main:app --reload
```

## Swagger Docs

Open:

http://127.0.0.1:8000/docs
