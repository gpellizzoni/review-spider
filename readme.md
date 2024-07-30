
# Review Fetcher

This project is a Flask application that fetches product reviews from different review providers (Yotpo and PowerReviews), handles pagination, and stores the reviews in a PostgreSQL database using SQLAlchemy.

## Requirements

- Python 3.7+
- PostgreSQL
- Virtual Environment (optional but recommended)

## Setup Instructions

1. **Install the dependencies**:

    ```sh
    pip install -r requirements.txt
    ```

2. **Set up the `.env` file**:

    Modify the `.env` file in the root with actual database credentials:

    ```plaintext
    DB_URL=postgresql://[USER]:[PASSWORD]@[HOST]:[PORT]/[DATABASE]
    ```

3. **Set up the database**:

    Run this script to create the database table

    ```sh
    python create_db.py
    ```

4. **Run the start the server locally**:

    ```sh
    python run.py
    ```

5. **Trigger the review fetching**:

    Send a request to `http://localhost:5000/fetch_reviews`

    ```sh
    curl "http://127.0.0.1:5000/fetch_reviews"
    ```

## Notes

- The application reads URLs from the `urls.txt` file and determines whether to fetch reviews from Yotpo or PowerReviews based on the URL.
- The reviews are fetched and stored in the PostgreSQL database.
