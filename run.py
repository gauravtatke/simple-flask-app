# In uwsgi, app is not run as <python> <app name> so the db import does not work.
# So separate file is created to import app, db and createall db.

from app import app
from db import db


@app.before_first_request
def create_tables():
    db.create_all()


db.init_app(app)
