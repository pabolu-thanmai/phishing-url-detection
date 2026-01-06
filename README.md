# Phishing URL Detection

## Overview
Phishing attacks commonly use deceptive URLs to trick users into revealing sensitive information.
This project detects whether a given URL is **phishing** or **legitimate** using machine learning
based solely on URL characteristics.

The focus of this project is to build a **lightweight, interpretable, URL-only detection system**
that can act as a first-line filter against phishing attempts.

---

## Problem Statement
Given a URL, predict whether it is phishing or legitimate using patterns present in the URL string
and its structural properties.

---

## Approach

### 1. Preprocessing
- Removed URL protocols (`http`, `https`)
- Normalized URLs to lowercase
- Retained only alphanumeric characters, dots, and slashes

### 2. Feature Engineering
Two categories of features were used:

**Textual Features**
- Character-level TF-IDF (n-grams from 2 to 5)
- Captures obfuscation patterns commonly used in phishing URLs

**Structural Features**
- URL length
- Number of digits
- Number of special characters
- Presence of IP address
- Number of subdomains
- Presence of suspicious keywords (e.g., login, secure, verify)

### 3. Model
- **Logistic Regression**
- Chosen for simplicity, interpretability, and strong performance on sparse text features

---

## Evaluation
- Precision, Recall, and F1-score were used for evaluation
- **Recall was prioritized**, as missing a phishing URL is more costly than flagging a legitimate one
- After feature engineering, phishing recall stabilized at approximately **92%**

Further improvements would require external context such as domain reputation or website content,
which was intentionally kept out of scope.

---

## Project Structure

phishing-url-detection/
│
├── data/
│ └── phishing_site_urls.csv
│
├── src/
│ ├── preprocess.py
│ ├── train.py
│ └── predict.py
│
├── model/
│ ├── model.pkl
│ └── vectorizer.pkl
│
├── README.md
└── requirements.txt


---

## How to Run

### 1. Train the model
python src/train.py

###2. Predict from command line
python src/predict.py "http://secure-login-update.example.com"


Output:

Prediction: Phishing

##Limitations

This is a URL-only detection system

It does not use domain reputation, DNS, or website content

Intended as a first-layer phishing filter, not a standalone security solution

##Future Improvements

Integrate domain reputation or blacklist-based signals

Combine with content-based or browser-side detection


