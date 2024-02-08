from models import db, Quote, Author, Category
from app import app

with app.app_context():
    print("🗑️ Removing existing seed data...")

    # Delete existing records in the quotes table
    db.session.query(Quote).delete()

    # Delete existing records in the authors table
    db.session.query(Author).delete()

    # Delete existing records in the category table
    db.session.query(Category).delete()

    db.session.commit()
    print("🗑️ Existing seed data removed.")

    print("📚 Seeding quotes with reviews...")

    quotes_data = [
      
        {"text": "In the end, it's not the years in your life that count. It's the life in your years.","author_id":1},
        {"text": "The greatest glory in living lies not in never falling, but in rising every time we fall.","author_id":2},
        {"text": "Success is not final, failure is not fatal: It is the courage to continue that counts.","author_id":3},
        {"text": "Your time is limited, so don't waste it living someone else's life.","author_id":4},
        {"text": "Life is like riding a bicycle. To keep your balance, you must keep moving.","author_id":5},
        {"text": "The only limit to our realization of tomorrow will be our doubts of today.","author_id":6},

    
    ]



    for quote_data in quotes_data:
        quote = Quote(**quote_data)
        db.session.add(quote)
    db.session.commit()


    authors_data = [
    
    {"name": "Abraham Lincoln", "nationality": "American"},
    {"name": "Nelson Mandela", "nationality": "South African"},
    {"name": "Winston Churchill", "nationality": "British"},
    {"name": "Steve Jobs", "nationality": "American"},
    {"name": "Albert Einstein", "nationality": "German-American"},
    {"name": "Franklin D. Roosevelt", "nationality": "American"},
 
    ]
    for author_data in authors_data:
        author=Author(**author_data)
        db.session.add(author)
    db.session.commit()

    categories_data = [
    
    {"name": "Motivational Quotes" ,"description": "Inspirational quotes to uplift spirits"}
    {"name": " Leadership Quotes " ,"description": "Quotes about leadership and success"}
    {"name": "Inspirational Quotes" ,"description": " Quotes to inspire and motivate"}
    {"name": " Success Quotes" ,"description": "Quotes about achieving success"}
    {"name": "Innovation Quotes" ,"description": "Quotes about creativity and innovation"}
    {"name": "Wisdom Quotes" ,"description": "Quotes containing wisdom and insight"}
    ]
    for category_data in categories_data:
        category=Category(**category_data)
        db.session.add(category)db.session.commit()
    print("📚 Done seeding!")
