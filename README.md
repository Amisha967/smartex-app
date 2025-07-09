# 💸 Smartex - SMS Expense Classifier

Smartex is an intelligent SMS classification app that uses Natural Language Processing (NLP) and machine learning to categorize bank-related SMS messages into meaningful labels such as `Income`, `Expense`, `Food`, `Utilities`, `Refund`, and more.

Built with:
- 🧠 Scikit-learn
- 🐼 Pandas
- 🔤 TF-IDF vectorizer
- 🌐 Streamlit for the UI
- 🐳 Docker for containerization

---

## 📂 Project Structure

```
smartex/
├── app/
│   └── streamlit_app.py      # Streamlit UI
├── data/
│   └── SMS-DATA-cleaned.csv  # Cleaned and labeled SMS data
├── model/
│   ├── model.pkl             # Trained ML model
│   └── vectorizer.pkl        # TF-IDF vectorizer
├── src/
│   ├── train.py              # Training script
│   ├── classify.py           # Predicts label for SMS
│   └── parser.py             # Extracts info (amount, keywords, etc.)
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation (Local)

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/smartex.git
cd smartex
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Train Model (Optional if model already exists)

```bash
python src/train.py
```

---

## 🚀 Run Streamlit App Locally

```bash
streamlit run app/streamlit_app.py
```

Visit [http://localhost:8501](http://localhost:8501) in your browser.

---

## 🐳 Run with Docker

### Build the Image

```bash
docker build -t smartex-app .
```

### Run the Container

```bash
docker run -p 8510:8501 smartex-app
```

Then open [http://localhost:8510](http://localhost:8510) in your browser.

> Note: The left-hand side (`8510`) is the **host port**, and `8501` is Streamlit’s **internal default port**.

---

## ✨ Features

- 🔍 Classifies SMS into custom categories.
- 📊 NLP-powered TF-IDF feature extraction.
- 🧪 Supports retraining with labeled SMS data.
- 🖥️ Clean, interactive UI with Streamlit.
- 📦 Dockerized for production ease.

---

## 🛠️ To Do / Improvements

- [ ] Improve class balance with more labeled data.
- [ ] Integrate deep learning models (BERT, etc.)
- [ ] Add filtering, export options in Streamlit UI.
- [ ] REST API endpoint for model predictions.

---

## 🧠 Model Info

- Model: `RandomForestClassifier`
- Vectorizer: `TfidfVectorizer (1,2)-gram`, `max_features=3000`
- Trained on ~850 labeled messages (and growing)

---

## 🤝 Contributing

PRs are welcome. Please label your PR with one of:
- `bug`
- `feature`
- `enhancement`
- `refactor`

---

## 📄 License

MIT License – Feel free to use and modify.

---

## 🙋‍♂️ Questions?

Open an issue or reach me via [LinkedIn](https://www.linkedin.com/in/amisha-kumari-87a510312/)
