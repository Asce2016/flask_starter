from . import db

class UserProfile(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    age = db.Column(db.Integer(20))
    gender = db.Column(db.CHAR(80))
    biography = db.Column(db.String(40))
    
    
    
            
            
    def __repr__(self):
        return '<User %r>' % (self.username)
