def clean_price(price_str):
    try:
        return float(price_str.replace('Â', '').replace('£', '').strip())
    except Exception:
        return None

def convert_rating(rating_str):
    mapping = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5
    }
    return mapping.get(rating_str, None)

def clean_data(raw_books):
    cleaned = []
    for book in raw_books:
        cleaned.append({
            "title": book["title"],
            "price": clean_price(book["price"]),
            "url": book["url"],
            "rating": convert_rating(book["rating"])
        })
    return cleaned
