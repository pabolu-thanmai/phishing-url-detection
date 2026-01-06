import re
import pandas as pd

def preprocess_url(url: str) -> str:
    """Clean and normalize a URL string."""
    if not isinstance(url, str):
        return ""
    # remove protocol
    url = re.sub(r"https?://", "", url)
    # keep only alphanumeric, dot and slash
    url = re.sub(r"[^a-zA-Z0-9./]", " ", url)
    return url.lower()

def extract_features(df: pd.DataFrame) -> pd.DataFrame:
    """Takes a DataFrame with a column 'URL' and
    returns the same DataFrame with engineered features."""
    df = df.copy()
    # cleaned URL
    df["clean_url"] = df["URL"].apply(preprocess_url)
    # structural features
    df["url_length"] = df["clean_url"].apply(len)
    df["num_special_chars"] = df["clean_url"].apply(
        lambda x: len(re.findall(r"[^a-zA-Z0-9]", x))
    )
    df["num_digits"] = df["clean_url"].apply(
        lambda x: sum(char.isdigit() for char in x)
    )
    # presence of IP address
    df["has_ip"] = df["clean_url"].apply(
        lambda x: 1 if re.search(r"\b\d{1,3}(\.\d{1,3}){3}\b", x) else 0
    )
    # subdomain count
    df["num_subdomains"] = df["clean_url"].apply(
        lambda x: max(x.count(".") - 1, 0)
    )
    # suspicious keyword presence
    suspicious_words = ["login", "secure", "verify", "update", "bank", "confirm"]
    df["has_suspicious_word"] = df["clean_url"].apply(
        lambda x: 1 if any(word in x for word in suspicious_words) else 0
    )

    return df
