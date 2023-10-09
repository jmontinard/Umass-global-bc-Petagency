"""Demo app using SQLAlchemy."""

from flask import Flask, request, redirect, render_template, flash, url_for
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SECRET_KEY'] = "SECRET!"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///petAgency'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
connect_db(app)
# db.create_all()

if __name__ == "__main__":
    # Create an application context before running create_all()
    with app.app_context():
        db.create_all()

toolbar = DebugToolbarExtension(app)



@app.route('/')
def show_home():
    """Displays the homepage"""
    pets = Pet.query.all()
    return render_template("home.html", pets=pets)


@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """adds pet"""

    form = AddPetForm()
    if form .validate_on_submit():
         name = form.name.data
         species = form.species.data
         age = form.age.data
         available = form.available.data
         new_pet = Pet(name =name, species=species, age=age, available=available)
         db.session.add(new_pet)
         db.session.commit()
         flash(f"{new_pet.name} added.")
        #  return redirect('/')
         return redirect(url_for('show_home'))


    else:
        return render_template("add_pet_form.html", form=form)


@app.route('/<int:pet_id>', methods =["GET","POST"])
def edit_pet(pet_id):
    """ edits the selected pet"""
    pet = Pet.query.get_or_404(pet_id)
    form  = EditPetForm(obj=pet)
    
    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        flash(f"{pet.name} has been edited")
        return redirect(url_for('show_home'))
        # return redirect(f"/{pet_id}")
    else:
        return render_template("editPetForm.html", form=form, pet=pet)

@app.route("/api/pets/<int:pet_id>", methods=['GET'])
def api_get_pet(pet_id):
    """Return basic info about pet in JSON."""

    pet = Pet.query.get_or_404(pet_id)
    info = {"name": pet.name, "age": pet.age}

    return jsonify(info)