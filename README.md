# SpamGuard – AI Spam & Phishing Detection System

SpamGuard is a machine learning based spam and phishing detection system designed to analyze text messages and emails for malicious content.

The system combines Natural Language Processing (NLP), URL analysis, and domain reputation checks to classify messages as **spam or legitimate**.

It also includes a REST API and browser extension support, allowing real-time scanning of suspicious messages.

---

# Features

### Machine Learning Spam Detection

* RandomForest classifier
* TF-IDF text vectorization
* High accuracy spam classification

### Phishing Detection

Detects common phishing indicators such as:

* suspicious domains
* shortened URLs
* IP-based URLs
* abnormal link length

### NLP Analysis

Uses TF-IDF to detect:

* spam keywords
* phishing phrases
* marketing spam patterns

### API Support

FastAPI backend allows:

* web apps
* browser extensions
* automated email scanners

### Browser Extension Integration

A browser extension can send messages to the backend API to determine whether content is spam.

---

# Project Structure

```
spam_guard/
│
├── api/
│   └── spam_api.py
│
├── data/
│   └── spam_dataset.csv
│
├── models/
│   ├── spam_model.pkl
│   └── tfidf_vectorizer.pkl
│
├── src/
│   ├── trainer.py
│   ├── predictor.py
│   ├── nlp_features.py
│   ├── url_features.py
│   └── reputation.py
│
├── extension/
│   ├── manifest.json
│   ├── popup.html
│   └── popup.js
│
├── requirements.txt
└── README.md
```

---

# Installation

Clone the repository

```
git clone https://github.com/YOUR_USERNAME/spam_guard.git
cd spam_guard
```

Create virtual environment

```
python -m venv venv
```

Activate environment

Linux / Mac

```
source venv/bin/activate
```

Windows

```
venv\Scripts\activate
```

Install dependencies

```
pip install -r requirements.txt
```

---

# Dataset

Place the training dataset in:

```
data/spam_dataset.csv
```

Dataset format:

```
text,label
message_text_here,0_or_1
```

Example:

```
text,label
Win a free iPhone now!,1
Let's meet tomorrow for lunch,0
```

Recommended datasets:

* SMS Spam Collection Dataset
* Enron Email Dataset
* SpamAssassin Public Corpus

---

# Training the Model

Run:

```
python src/trainer.py
```

This will generate:

```
models/spam_model.pkl
models/tfidf_vectorizer.pkl
```

---

# Running the API

Start the FastAPI server:

```
uvicorn api.spam_api:app --reload
```

API will run at:

```
http://127.0.0.1:8000
```

Interactive documentation:

```
http://127.0.0.1:8000/docs
```

---

# API Usage Example

Request

```
POST /scan
```

Example JSON request

```
{
"text": "Congratulations! You won a free prize. Click here!"
}
```

Example response

```
{
"prediction": "spam",
"confidence": 0.97
}
```

---

# Browser Extension

The extension sends message text to the backend API and displays whether it is spam.

Steps:

1. Open Chrome Extensions
2. Enable Developer Mode
3. Click **Load unpacked**
4. Select the `extension/` folder

You can now test messages through the popup interface.

---

# Detection Pipeline

```
User Message
     │
     ▼
Feature Extraction
     │
     ├─ TF-IDF NLP analysis
     ├─ URL feature extraction
     └─ Domain reputation check
     │
     ▼
RandomForest Model
     │
     ▼
Spam / Not Spam Classification
```

---

# Future Improvements

Possible upgrades include:

* BERT based spam classification
* VirusTotal URL reputation integration
* Gmail API integration
* Email header analysis (SPF, DKIM, DMARC)
* phishing domain blacklist
* real-time email scanning

---


