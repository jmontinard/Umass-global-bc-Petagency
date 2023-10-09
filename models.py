from flask_sqlalchemy import SQLAlchemy
from wtforms.validators import InputRequired, Optional, Email

img_url="https://images.unsplash.com/photo-1505628346881-b72b27e84530?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=987&q=80"
db = SQLAlchemy()



def connect_db(app):
    """Connect this database to provided Flask app.

    You should call this in your Flask app.
    """

    db.app = app
    db.init_app(app)


class Pet(db.Model):
    """pet to adpot."""

    __tablename__ = "pets"

    id = db.Column(db.Integer,
                   primary_key=True)
    name = db.Column(db.Text,
                     nullable=False)
    species = db.Column(db.Text,
                     nullable=False)
    photo_url = db.Column(db.Text,
                      default=img_url)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean,
                    nullable = False,
                    default=True)
    def stock_or_image_url(self):
        """ this will always defualt to stock img if no image is uploaded """
        return self.photo_url or img_url
# class Pet(db.Model):
#     """Adoptable pet."""

#     __tablename__ = "pets"

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.Text, nullable=False)
#     species = db.Column(db.Text, nullable=False)
#     photo_url = db.Column(db.Text)
#     age = db.Column(db.Integer)
#     notes = db.Column(db.Text)
#     available = db.Column(db.Boolean, nullable=False, default=True)

#     def image_url(self):
#         """Return image for pet -- bespoke or generic."""

#         return self.photo_url or img_url


