import re

def get_keywords(product: str):
    """
    Returns 3–4 short SEO-friendly keywords based on the product name.
    """
    # Clean product name: remove symbols, extra text
    base = re.sub(r"[^a-zA-Z0-9 ]", "", product)  # Remove brackets and special chars
    base = base.lower().strip()
    base = base.split(" - ")[0]  # Take only the first part before hyphen

    # Optional: Keep only first few words
    base_words = base.split()
    short_base = " ".join(base_words[:4])  # max 4 words

    # Return list of SEO keywords
    return [
        short_base,
        f"best {short_base} online",
        f"{short_base} price",
        f"buy {short_base}"
    ]
