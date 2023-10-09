from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField, SelectField, TextAreaField
from wtforms.validators import InputRequired, Length, NumberRange, URL, Optional


class AddPetForm(FlaskForm):
    """Form for adding pets."""
    name = StringField("Pet Name", validators=[
                       InputRequired(message="Pet Name can't be blank")])
    species = SelectField(
        "Species",
        choices=[("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine")],
    )
    # species = StringField("species", validators=[
    #                    AnyOf(values=("cat", "dog", "porcupine"), message="Please enter either a cat, dog, or porcupine")])
    photo_url = StringField("Photo Url", validators=[Optional(), URL(require_tld=True, message="Please enter a valid Url") ])
    age = IntegerField("Age", validators=[NumberRange(min=0, max=30, message="Enter an age between 0-30")])
    notes = TextAreaField("Notes", validators=[Optional(), Length(min=10)])
    available =  BooleanField("Available")

class EditPetForm(FlaskForm):
   """Edit Pet form  """
   photo_url = StringField("Photo Url", validators=[Optional(), URL(require_tld=True, message="Please enter a valid Url")])

   notes = TextAreaField("Notes", validators=[Optional(), Length(min=10)])

   available =  BooleanField("Available")
