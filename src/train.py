import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.ensemble import RandomForestClassifier
import joblib
from sklearn.svm import LinearSVC
# Load dataset
df = pd.read_csv("data/SMS-DATA-cleaned.csv", encoding="ISO-8859-1")
df.columns = df.columns.str.strip().str.lower()
# Remove labels that occur only once
df = df[df['label'].map(df['label'].value_counts()) > 1]

# Filter out unlabeled rows
df = df[df["label"].notnull() & (df["label"] != "")]

print(f"✅ Using {len(df)} labeled rows for training.")

# Features and labels
X = df["text"]
y = df["label"]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

# Vectorizer
vectorizer = TfidfVectorizer(ngram_range=(1, 2), max_features=3000)
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)
print("Label distribution:\n", df["label"].value_counts())
# Model
# clf = LogisticRegression(max_iter=1000)
# clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf = LinearSVC()
clf.fit(X_train_vec, y_train)

print("Training on", len(df), "labeled rows.")
print("Label distribution:\n", df["label"].value_counts())

# Evaluation
y_pred = clf.predict(X_test_vec)
print(classification_report(y_test, y_pred))

# Save model and vectorizer
joblib.dump(clf, "model/model.pkl")
joblib.dump(vectorizer, "model/vectorizer.pkl")
print("✅ Model and vectorizer saved.")