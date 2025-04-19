from scraper.cleaner import clean_price, convert_rating

def test_clean_price():
    assert clean_price("£12.99") == 12.99
    assert clean_price("invalid") is None

def test_convert_rating():
    assert convert_rating("Three") == 3
    assert convert_rating("Unknown") is None
