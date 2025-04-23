# 📧 Email Spam Classification Backend

This project is a Natural Language Processing (NLP) based email spam classification backend built using
**Python**, **Jupyter Notebook**, and **Flask**. 
It allows users to input an email message and receive a prediction—Spam or Not Spam—based on the trained model.


## 🚀 Features

- Detects whether an email is spam or not
- Uses NLP techniques for text preprocessing
- Flask-based API backend for integration with any frontend
- Model trained in Jupyter Notebook using sklearn & NLP pipeline

---

## 🛠️ Tech Stack

- **Python**
- **Flask** (Backend API)
- **Jupyter Notebook** (Model development)
- **scikit-learn**
- **NLTK** for text preprocessing

---

## 🧠 How it Works

1. Input message is sent to the backend.
2. The text is cleaned, tokenized, and transformed using NLP techniques.
3. A trained ML model (e.g., Naive Bayes / Logistic Regression) predicts if it's spam.
4. The response is returned as `Spam` or `Not Spam`.
