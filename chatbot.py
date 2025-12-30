import json
import pickle
import random


model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

with open("intents.json") as f:
    intents = json.load(f)

def chatbot_response(text):
    text = text.lower() 
    X = vectorizer.transform([text])
    intent = model.predict(X)[0]

    for i in intents["intents"]:
        if i["tag"] == intent:
            return random.choice(i["responses"])

    return "Sorry, I did not understand."
