from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, validators, DateField, TimeField, FileField, RadioField
#from wtforms.validators import DataRequired

#simple formulaire
class loginForm(FlaskForm):
    name = StringField("Nom d'utilisateur",[validators.InputRequired()])
    password = PasswordField("Mot de passe",[validators.InputRequired()])
    submit = SubmitField("Login")

class addEventForm(FlaskForm):
    description = StringField("Titre de l'événement",[validators.InputRequired()])
    date_debut = DateField("Date début de l'événement", [validators.InputRequired()])
    date_fin = DateField("Date de fin de l'événement")
    heure_debut = TimeField("Heure de début de l'événement", [validators.InputRequired()])
    heure_fin = TimeField("Heure de fin de l'événement")
    lieu = StringField("Titre de l'événement",[validators.InputRequired()])
    vignette = FileField("Sélectionnez une éventuelle vignette pour l'événement")
    visibilité = RadioField("Qui peut voir cet événement",choices=["Tout le monde (événement public)", "Les membres du choeur", "Les membres de la maîtrise"])
