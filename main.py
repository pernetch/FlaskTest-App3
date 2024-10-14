
import os
from app import create_app, db
from app.models import User, Role, Event, Visibility, Group

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role, Event=Event, Visibility=Visibility, Group=Group)


if __name__ == '__main__':
    app.run(debug=True)