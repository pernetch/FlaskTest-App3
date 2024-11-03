from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, validators
#from wtforms.validators import DataRequired

#simple formulaire
class loginForm(FlaskForm):
    name = StringField("Nom d'utilisateur",[validators.InputRequired()])
    password = PasswordField("Mot de passe",[validators.InputRequired()])
    submit = SubmitField("Login")