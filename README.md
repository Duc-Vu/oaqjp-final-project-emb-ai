## Final Project

## 📌 Overview

This project is a simple AI-powered web application that detects emotions from input text using IBM Watson NLP.
It processes user input, analyzes emotional tone, and returns structured results through a REST API built with Flask.

---

## 🚀 Features

* Detect emotions from text input
* Returns scores for:
  * anger
  * disgust
  * fear
  * joy
  * sadness
* Identifies the **dominant emotion**
* REST API using Flask
* Includes unit tests and error handling

---

## 🧱 Project Structure

```
project/
│
├── emotion_detection/
│   ├── __init__.py
│   └── emotion_detection.py
│
├── app.py
├── test_emotion_detection.py
├── requirements.txt
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone <your-repo-url>
cd <project-folder>
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

Start the Flask server:

```bash
python3 app.py
```

The application will run on:

```
http://127.0.0.1:5000
```

---

## 🧪 Testing the API

### Using curl

```bash
curl -X POST http://127.0.0.1:5000/emotion \
-H "Content-Type: application/json" \
-d '{"text":"I love AI"}'
```

---

### Example Response

```json
{
  "anger": 0.02,
  "disgust": 0.01,
  "fear": 0.03,
  "joy": 0.92,
  "sadness": 0.05,
  "dominant_emotion": "joy"
}
```

---

## 🧪 Running Unit Tests

```bash
python3 -m unittest
```

---

## ⚠️ Error Handling

* Returns error if input text is empty
* Handles API failures gracefully

---

## 🧹 Code Quality

Run static analysis:

```bash
flake8 .
```

---

## 🧠 Notes

* The application uses a pre-trained Watson NLP model
* No model training is required
* Designed as a lightweight demonstration of an AI-powered API system

---

## 📎 License

This project is for educational purposes.
