
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#tables de la DB en SQLALCHEMY
class Role (db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    description = db.Column(db.String(100))
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Role %r>' % self.name


class User (db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True)
    password = db.Column(db.String(256))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' % self.name
    

  

class Visibility (db.Model):
    __tablename__ = 'visibilities'
    id = db.Column(db.Integer, primary_key=True)
    visibility = db.Column(db.String(10))
    events = db.relationship('Event', backref='visibility', lazy='dynamic')

    def __repr__(self):
        return '<Role %r>' % self.name
    
class Group (db.Model):
    __tablename__ = 'groupes'
    id = db.Column(db.Integer, primary_key=True)
    groupe = db.Column(db.String(64), unique=True)
    events = db.relationship('Event', backref='groupe', lazy='dynamic')

    def __repr__(self):
        return '<Role %r>' % self.name
    
class Event (db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    date_start = db.Column(db.Date)
    date_end = db.Column(db.Date)
    time_start = db.Column(db.Time)
    time_end = db.Column(db.Time)
    description = db.Column(db.String(256))
    lieu = db.Column(db.String(50))
    vignette_name = db.Column(db.String(100))
    visibility_id = db.Column(db.Integer, db.ForeignKey('visibilities.id'))
    groupe_id = db.Column(db.Integer, db.ForeignKey('groupes.id'))
    
    def __repr__(self):
        return '<Event %r>' % self.description