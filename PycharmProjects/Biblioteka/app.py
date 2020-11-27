from flask import Flask, render_template, request
from data_management import add_author, get_all_authors, add_book, get_all_books
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('base.html')

@app.route("/dodaj_autora/", methods=['GET', 'POST'])
def dodaj_autora():
    if request.method == 'POST':
        imie = request.form['imie']
        nazwisko = request.form.get('nazwisko')
        add_author(imie, nazwisko)
    a = render_template('dodaj_autora.html')
    return a

@app.route("/dodaj_ksiazke/", methods=['GET', 'POST'])
def dodaj_ksiazke():
    if request.method == 'POST':
        tytul = request.form['tytul']
        add_book(tytul)
    a = render_template('dodaj_ksiazke.html')
    return a


@app.route("/wyswietl_autora/")
def wyswietl_autora():
    authors = get_all_authors()
    a = render_template('wyswietl_autora.html', authors=authors)
    return a

@app.route("/wyswietl_ksiazki/")
def wyswietl_ksiazki():
    books = get_all_books()
    a = render_template('wyswietl_ksiazki.html', books=books)
    return a

if __name__ == '__main__':
    app.run()
