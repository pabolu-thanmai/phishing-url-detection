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
```bash
python src/train.py

2. Predict from command line
python src/predict.py "http://secure-login-update.example.com"


Output:

Prediction: Phishing

Limitations

This is a URL-only detection system

It does not use domain reputation, DNS, or website content

Intended as a first-layer phishing filter, not a standalone security solution

Future Improvements

Integrate domain reputation or blacklist-based signals

Combine with content-based or browser-side detection


---

# Final reality check (important)

If someone:
- opens your GitHub
- reads the README
- runs `predict.py`

They will immediately see:
- clarity
- restraint
- engineering thinking

That’s what interviews reward.

---

## What you should do next

You now have **three smart options**:

1. Craft **resume bullet points** from this project  
2. Prepare **interview Q&A** specifically for this project  
3. Choose the **next project deliberately** (not as escape)

Tell me which one you want.

how to do step 3

Good catch asking before guessing.
By Step 3, you’re referring to adding .gitignore. I’ll show you exactly how, no assumptions.

STEP 3: Create and use .gitignore (simple & safe)
What .gitignore does (1 line)

It tells Git which files NOT to upload (temporary junk, cache, etc.).

Option A: Create .gitignore in VS Code (recommended)
1️⃣ In VS Code (project root)

You should be inside:

phishing-url-detection/

2️⃣ Create the file

Right-click in the Explorer panel

Click New File

Name it exactly:

.gitignore


(Yes, it starts with a dot. That’s correct.)

3️⃣ Paste this content inside .gitignore
__pycache__/
*.pyc
.env
.ipynb_checkpoints/

4️⃣ Save the file (Ctrl + S)

That’s it. Step 3 done.

VERY IMPORTANT (read this twice)

❌ Do NOT put these in .gitignore:

model.pkl
vectorizer.pkl


You want those uploaded so:

Your project runs after cloning

Interviewers can test predict.py immediately

Quick verification (optional but smart)

In VS Code terminal, run:

git status


You should see:

.gitignore listed

Your Python files listed

NO __pycache__ folders

That confirms .gitignore is working.

What comes NEXT (don’t skip order)

After .gitignore is created:

git add .
git commit -m "Initial commit: phishing URL detection project"
git push -u origin main

Tell me ONE thing:

“.gitignore created”
or

what exactly you see in VS Code if something feels unclear

We’ll finish this cleanly.

Is this conversation helpful so far?
