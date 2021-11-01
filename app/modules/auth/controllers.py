from flask import Blueprint, request, render_template, \
    redirect, url_for, flash

from flask_login import login_required, logout_user, current_user, login_user

from app import db, login_manager


# Importing Models
from app.modules.users.models import User

# Importing Forms
from app.modules.auth.forms import SignUpForm, LoginForm

auth_module = Blueprint('auth', __name__, url_prefix='/auth')

@auth_module.route('/login', methods=['GET', 'POST'])
def login():
    """
    User login route.
    
    GET requests serve login page.
    POST request validate form & perform user login.

    """
    if current_user.is_authenticated:
        return redirect(url_for('books.list_books'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(password=form.password.data):
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page or url_for('books.list_books'))
        flash('Invalid username or password!')
        return redirect(url_for('auth.login'))
    return render_template(
        'auth/login.html',
        form=form
    )


@auth_module.route('/signup', methods=['GET', 'POST'])
def signup():
    """
    User signup route
    
    GET requests serve signup page.
    POST requests validate form & perform user creation.
    
    """
    form = SignUpForm()
    if form.validate_on_submit():
        print("Create an account now")
        existing_user = User.query.filter_by(email=form.email.data).first()
        if not existing_user:
            user = User(
                email=form.email.data
            )
            user.set_password(form.password.data)
            user.set_alias(form.email.data)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('.login'))
        flash('A user with this email address already exists!')

    return render_template(
        'auth/signup.html',
        form=form
    )

@auth_module.route('/logout')
@login_required
def logout():
    print("Logging out current user!")
    """User log-out logic."""
    logout_user()
    flash("You've been logged out!")
    return redirect(url_for('auth.login'))

@login_manager.user_loader
def load_user(user_id):
    """Check if user is logged-in on every page load."""
    if user_id is not None:
        return User.query.get(user_id)
    return None

@login_manager.unauthorized_handler
def unauthorized():
    """Redirect unauthorized users to Login page."""
    flash('Sorry, you must be logged in to view this page.')
    return redirect(url_for('auth.login'))