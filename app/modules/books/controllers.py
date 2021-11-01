from flask import Blueprint, request, render_template, \
    redirect, url_for

from flask_login import login_required

from app import db

# Importing Models
from app.modules.books.models import Book

# Importing Forms
from app.modules.books.forms import BookForm


book_module = Blueprint('books', __name__, url_prefix='/books')

@book_module.route('/', methods=['GET'])
@book_module.route('/list', methods=['GET'])
@login_required
def list_books():
    books = Book.query.all()
    # TODO: Implement pagination mechanism
    return render_template('books/list_books.html', books=books)


@book_module.route('/edit/<int:book_id>', methods=['GET', 'POST'])
def edit_book(book_id):

    book = Book.query.get_or_404(book_id)
    form = BookForm(obj=book)

    if request.method == 'GET':
        return render_template('books/edit_book.html', form=form)

    if request.method == 'POST' and form.validate_on_submit():
        book = Book.query.get(book_id)

        # TODO: only wupdate the items in the book that are different
        for key, value in form.data.items():
            setattr(book, key, value)

        db.session.commit()

        return redirect(url_for('.list_books'))


@book_module.route('/add', methods=['GET', 'POST'])
@login_required
def add_book():
    form = BookForm()

    if form.validate_on_submit():
        book = Book(title=form.title.data,
            author=form.author.data,
            genre=form.genre.data,
            release_year=form.release_year.data
            )

        db.session.add(book)
        db.session.commit()

        return redirect(url_for('.list_books'))
    return render_template('books/add_book.html', form=form)


@book_module.route('/delete/<int:book_id>', methods=['GET'])
@login_required
def delete(book_id):
    book = Book.query.get(book_id)

    if not book:
        # TODO: Flash a message
        return redirect(url_for('.list_books'))

    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('.list_books'))
