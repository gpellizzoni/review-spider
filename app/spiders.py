import requests
from app import db
from app.models import Review
from app.utils import convert_timestamp_to_date

def fetch_and_store_yotpo_reviews(base_url):
    page = 1
    max_pages = 50

    while page <= max_pages:
        response = requests.get(f"{base_url}&page={page}")
        data = response.json()
        
        if 'response' not in data or 'reviews' not in data['response']:
            break
        
        reviews = data['response']['reviews']
        if not reviews:
            break
        
        for review in reviews:
            new_review = Review(
                id=review['id'],
                score=review['score'],
                content=review['content'],
                title=review['title'],
                created_at=review['created_at'],
                user_display_name=review['user']['display_name']
            )
            db.session.add(new_review)
        
        db.session.commit()
        page += 1

def fetch_and_store_powerreviews_reviews(base_url):
    current_page_number = 1
    max_pages = 50
    page_size = 25

    while current_page_number <= max_pages:
        response = requests.get(f"{base_url}&paging.from={(current_page_number - 1) * page_size}&paging.size={page_size}")
        data = response.json()
        
        if 'reviews' not in data['results'][0]:
            break
        
        reviews = data['results'][0]['reviews']
        if not reviews:
            break
        
        for review in reviews:
            new_review = Review(
                id=review['review_id'],
                score=review['metrics']['rating'],
                content=review['details']['comments'],
                title=review['details']['headline'],
                created_at=convert_timestamp_to_date(review['details']['created_date']),
                user_display_name=review['details']['nickname']
            )
            db.session.add(new_review)
        
        db.session.commit()
        
        # Check if there is a next page
        paging = data.get('paging', {})
        next_page_url = paging.get('next_page_url')
        if not next_page_url:
            break
        
        current_page_number += 1

def fetch_reviews():
    urls_file = './urls.txt'
    with open(urls_file, 'r') as file:
        urls = [line.strip() for line in file if line.strip()]

    for url in urls:
        if 'yotpo' in url:
            fetch_and_store_yotpo_reviews(url)
        elif 'powerreviews' in url:
            fetch_and_store_powerreviews_reviews(url)