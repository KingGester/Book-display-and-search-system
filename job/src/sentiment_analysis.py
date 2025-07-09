from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import re

# ------------------ Text Cleaning ------------------
def clean_text(text):
    text = re.sub(r"http\S+", "", str(text))       # remove URLs
    text = re.sub(r"[^\w\s]", "", text)           # remove punctuation
    text = re.sub(r"\d+", "", text)                # remove numbers
    text = text.lower().strip()
    return text

def preprocess_df(df, text_col="Text"):
    df[text_col] = df[text_col].apply(clean_text)
    return df

# ------------------ Feature Extraction ------------------
def vectorize_texts(texts):
    vectorizer = TfidfVectorizer(
        max_features=5000,
        ngram_range=(1, 2),
        min_df=2,
        stop_words='english'
    )
    X = vectorizer.fit_transform(texts)
    return X, vectorizer

# ------------------ Model Training ------------------
def train_model(X, y):
    model = LogisticRegression(max_iter=1000, class_weight='balanced')
    model.fit(X, y)
    return model

# ------------------ Evaluation ------------------
def evaluate_model(model, X_test, y_test):
    preds = model.predict(X_test)
    print("\n[INFO] Classification Report:")
    print(classification_report(y_test, preds, zero_division=0))
    print("\n[INFO] Confusion Matrix:")
    cm = confusion_matrix(y_test, preds)
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.title("Confusion Matrix")
    plt.tight_layout()
    plt.show()

# ------------------ Predicting New Texts ------------------
def predict_sentiment(model, vectorizer, texts):
    texts_clean = [clean_text(t) for t in texts]
    X = vectorizer.transform(texts_clean)
    return model.predict(X)

# ------------------ Plot Distribution ------------------
def plot_sentiment_distribution(y):
    plt.figure(figsize=(6, 6))
    y.value_counts().plot.pie(autopct='%1.1f%%', startangle=90, colors=sns.color_palette("Set2"))
    plt.title("Sentiment Distribution")
    plt.ylabel("")
    plt.tight_layout()
    plt.show()
