from app import db

class Base(db.Model):

    __abstract__  = True

    id            = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date_created  = db.Column(db.DateTime,  default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime,  default=db.func.current_timestamp(),
                                            onupdate=db.func.current_timestamp())

    # User Ids that have created and modified the record
    created_by    = db.Column(db.Integer)
    modified_by    = db.Column(db.Integer)


class Book(Base):

    # Overriding default table name
    __tablename__   = 'books'

    # Book Name
    title           = db.Column(db.String(255), nullable=False, unique=True)
    author          = db.Column(db.String(128))
    genre           = db.Column(db.String(128))
    release_year    = db.Column(db.Integer)

    def __repr__(self):
        return "<Book :: ID {} - {}>".format(self.id, self.title)