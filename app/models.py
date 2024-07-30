from app import db

class Review(db.Model):
    __tablename__ = 'reviews'
    
    id = db.Column(db.Integer, primary_key=True)
    score = db.Column(db.Float)
    content = db.Column(db.Text)
    title = db.Column(db.String(255))
    created_at = db.Column(db.DateTime)
    user_display_name = db.Column(db.String(255))

    def __init__(self, id, score, content, title, created_at, user_display_name):
        self.id = id
        self.score = score
        self.content = content
        self.title = title
        self.created_at = created_at
        self.user_display_name = user_display_name
