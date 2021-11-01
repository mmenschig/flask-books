from app import db

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    """User account model."""

    # Overriding default table name
    __tablename__   = 'users'

    id              = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email           = db.Column(db.String(255), nullable=False, unique=True)
    alias           = db.Column(db.String(64), nullable=False)
    password        = db.Column(db.String(255), unique=False, nullable=False)
    role            = db.Column(db.String(64), default='user')
    status          = db.Column(db.String(64), default='inactive')
    created_on      = db.Column(db.DateTime, default=db.func.current_timestamp())
    last_login      = db.Column(db.DateTime, onupdate=db.func.current_timestamp())


    # Class properties
    @property
    def get_status(self):
        """Get the current user status"""
        return self.status

    def set_alias(self, email):
        self.alias = email.split("@")[0]

    # Class methods
    def set_password(self, password):
        """Create hashed password"""
        self.password = generate_password_hash(
            password,
            method='sha256'
        )

    def check_password(self, password):
        """Check hashed password"""
        return check_password_hash(self.password, password)


    def __repr__(self):
        return '<User {}>'.format(self.email)
