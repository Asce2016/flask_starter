from . import db

class UserProfile(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(80))
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    date = db.Column(db.String(80))
    age = db.Column(db.Integer)
    gender = db.Column(db.CHAR(2))
    biography = db.Column(db.String(40))
    
    
    def __init__(self, user_name, first_name, last_name, age, gender, biography,date):
        
        self.user_name = user_name
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.biography = biography
        self.date = date
        
        
            
            
    def __repr__(self):
        return '<User %r>' % (self.username)
