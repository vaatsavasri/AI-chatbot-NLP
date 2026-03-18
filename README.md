AI Chatbot using NLP

An intelligent **AI Chatbot** built using **Python and Natural Language Processing (NLP)** that classifies user intent and generates meaningful responses using machine learning techniques.



 Project Overview

This project focuses on building a chatbot that understands user input and responds intelligently by:

- Classifying user intent using NLP techniques  
- Applying machine learning models for prediction  
- Generating dynamic responses  

The chatbot is deployed using a **Streamlit web interface** for interactive usage.



 Features

-  **Intent Classification** — Uses TF-IDF vectorization and Logistic Regression  
-  **Dynamic Responses** — Randomized responses for better interaction  
- **Web Interface** — Interactive chatbot UI using Streamlit  
-  **Fast Processing** — Lightweight and efficient model  

---

##  Tech Stack

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![NLTK](https://img.shields.io/badge/NLTK-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit-Learn-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)


## Project Structure

```bash
ai-chatbot-nlp/
│
├── data/
│   └── intents.json          # Training data
│
├── model/
│   └── chatbot_model.pkl     # Trained model
│
├── app.py                    # Streamlit chatbot app
├── train.py                  # Model training script
├── utils.py                  # Helper functions
├── requirements.txt
└── README.md
