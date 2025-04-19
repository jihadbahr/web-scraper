from scraper.scraper import get_all_books
from scraper.cleaner import clean_data
from scraper.db_utils import save_to_db

def main():
    raw_books = get_all_books()
    cleaned_books = clean_data(raw_books)
    save_to_db(cleaned_books)
    print("✅ Data saved to SQLite database.")

if __name__ == "__main__":
    main()