# Add any model classes for Flask-SQLAlchemy here
from . import db
#from datetime import date

class Movie(db.Model):

    __tablename__='movies'

    id = db.Column(db.Integer, primary_key=True)
    title= db.Column(db.String(255))
    description= db.Column(db.String(255))
    poster= db.Column(db.String(255))
    created_at= db.Column(db.DateTime())

    def __init__(self,title,description,poster,created_at):
        self.title = title
        self.description = description
        self.poster = poster
        self.created_at = created_at

