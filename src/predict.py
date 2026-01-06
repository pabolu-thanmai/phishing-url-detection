import sys
import pickle
import pandas as pd
import re

from scipy.sparse import hstack
from preprocess import preprocess_url


def main():
    # 1. Read URL from command line
    if len(sys.argv) != 2:
        print("Usage: python predict.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    # 2. Preprocess URL
    clean_url = preprocess_url(url)

    # 3. Create DataFrame
    df = pd.DataFrame({"URL": [url]})
    df["clean_url"] = [clean_url]

    # 4. Handcrafted features (MUST match train.py)
    df["url_length"] = df["clean_url"].apply(len)

    df["num_special_chars"] = df["clean_url"].apply(
        lambda x: len(re.findall(r"[^a-zA-Z0-9]", x))
    )

    df["num_digits"] = df["clean_url"].apply(
        lambda x: sum(char.isdigit() for char in x)
    )

    df["has_ip"] = df["clean_url"].apply(
        lambda x: 1 if re.search(r"\b\d{1,3}(\.\d{1,3}){3}\b", x) else 0
    )

    df["num_subdomains"] = df["clean_url"].apply(
        lambda x: max(x.count(".") - 1, 0)
    )

    suspicious_words = ["login", "secure", "verify", "update", "bank", "confirm"]
    df["has_suspicious_word"] = df["clean_url"].apply(
        lambda x: 1 if any(word in x for word in suspicious_words) else 0
    )

    # 5. Load vectorizer and model
    with open("C:\\Users\\thanm\\OneDrive\\Documents\\phishing-url-detection\\model\\vectorizer.pkl", "rb") as f:
        vectorizer = pickle.load(f)

    with open("C:\\Users\\thanm\\OneDrive\\Documents\\phishing-url-detection\\model\\model.pkl", "rb") as f:
        model = pickle.load(f)

    # 6. TF-IDF transform
    X_tfidf = vectorizer.transform(df["clean_url"])

    handcrafted_features = df[
        [
            "url_length",
            "num_special_chars",
            "num_digits",
            "has_ip",
            "num_subdomains",
            "has_suspicious_word",
        ]
    ].values

    X = hstack([X_tfidf, handcrafted_features])

    # 7. Prediction
    prediction = model.predict(X)[0]

    if prediction == 1:
        print("Prediction: Phishing")
    else:
        print("Prediction: Legitimate")


if __name__ == "__main__":
    main()
