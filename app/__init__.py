import os, sys


from flask import Flask, render_template, redirect
from flask.helpers import url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def not_found(error):
    return render_template('500.html'), 500

@app.route('/')
def index():
    return redirect(url_for('.books.list_books'))

# Parsing out script arguments to
# determine which configuration to load
environment = os.environ["FLASK_ENV"]

# Configuration
if environment == 'production':
    print("INFO Loading Production Config")
    app.config.from_object('config.ProductionConfig')

elif environment == 'development':
    print("INFO Loading Development Config")
    app.config.from_object('config.DevelopmentConfig')

else:
    print("INFO Loading Testing Config")
    app.config.from_object('config.TestingConfig')


#  Initialize Plugins
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)


# Registering Blueprints
from app.modules.books.controllers import book_module
app.register_blueprint(book_module)

from app.modules.auth.controllers import auth_module
app.register_blueprint(auth_module)

# Build the database
db.create_all()

from app.modules.users.models import User

# Creating admin user if doesn't exist
user = User.query.filter_by(email='admin@admin.com').first()
if not user:
    print("Admin user doesn't exist - creating one now.")
    admin = User(
        email='admin@admin.com', 
        role="admin", 
        status="active"
    )
    admin.set_alias('admin@admin.com')
    admin.set_password(app.config["X_ADMIN_PASSWORD"] or 'admin') # Change this password in config.py
    db.session.add(admin)
    db.session.commit()
else:
    print("Admin user exists - taking no action.")

# TODO: Create admin user here