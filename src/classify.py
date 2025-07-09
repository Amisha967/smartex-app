import joblib

model = joblib.load("model.pkl")

def classify_sms(message):
    if not isinstance(message, str):
        return "Unknown"  # or "Unclassified"

    return model.predict([message])[0]