from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DecimalField
from wtforms.validators import DataRequired
import requests

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

MOVIE_DB_API_KEY = 'a5a369d4e71e2f305e40522a20013745'
tmdb_api_read_token = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJhNWEzNjlkNGU3MWUyZjMwNWU0MDUyMmEyMDAxMzc0NSIsInN1YiI6IjY1NTc1ZTJmZDA1MWQ5MDEwMDg1NWEwNiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.dJY_QITG-aBwkbJkHALNkuQuSFnwnlsj_ajf8H4R1QQ'
MOVIE_DB_SEARCH_URL = 'https://api.themoviedb.org/3/search/movie'
MOVIE_DB_DETAIL_URL = 'https://api.themoviedb.org/3/movie/'
# MOVIE_DB_IMG_URL='https://image.tmdb.org/t/p/w500'
MOVIE_DB_IMG_URL = 'https://image.tmdb.org/t/p/original'

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movie-collection.db"
Bootstrap5(app)
db = SQLAlchemy()
db.init_app(app)


class EditForm(FlaskForm):
    rating = DecimalField('Your Rating Out of 10 e.g. 7.5',
                          validators=[DataRequired(message="Field must be numeric e.g 8.3.")])
    review = StringField('Your Review', validators=[DataRequired(message="Enter your review.")])
    submit = SubmitField(label="Done")


class AddForm(FlaskForm):
    movie_title = StringField('Movie Title', validators=[DataRequired()])
    submit = SubmitField(label='Add Movie')


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return f'<Movie {self.title} - {self.year} - {self.description} - {self.rating} - {self.ranking} - {self.img_url}>'


with app.app_context():
    # db.drop_all()
    db.create_all()

@app.route("/")
def home():
    all_movies = db.session.execute(db.select(Movie).order_by(Movie.rating.desc())).scalars().all()
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    return render_template("index.html", movies=all_movies)


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    edit_form = EditForm()
    the_movie = db.get_or_404(Movie, id)
    if edit_form.validate_on_submit():
        if request.method == 'POST':
            the_movie.review = request.form['review']
            the_movie.rating = request.form['rating']
            db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", form=edit_form, movie=the_movie)


@app.route('/<int:id>')
def delete(id):
    movie_to_delete = db.get_or_404(Movie, id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/add', methods=['GET', 'POST'])
def add():
    add_form = AddForm()
    if add_form.validate_on_submit():
        the_movie_title = request.form['movie_title']
        # url=f'https://api.themoviedb.org/3/search/movie?query={the_movie_title}&api_key={tmdb_api_key}'
        response = requests.get(MOVIE_DB_SEARCH_URL, params={"api_key": MOVIE_DB_API_KEY, "query": the_movie_title})
        data = response.json()['results']
        return render_template("select.html", title_options=data)
    return render_template('add.html', form=add_form)


@app.route('/find')
def find_movie():
    movie_id = request.args.get('id')
    if movie_id:
        movie_api_detail_url = f'{MOVIE_DB_DETAIL_URL}/{movie_id}'
        response = requests.get(movie_api_detail_url, params={'api_key': MOVIE_DB_API_KEY, 'language': 'en-US'})
        data = response.json()
        new_movie = Movie(
            title=data['title'],
            year=data['release_date'].split("-")[0],
            img_url=f"https://image.tmdb.org/t/p/original/{data['poster_path']}",  # {data['poster_path']}",
            description=data['overview'],
            rating=data['vote_average'],
            ranking=0,
            review=""
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("rate_movie", id=new_movie.id))


@app.route("/edit", methods=['GET', 'POST'])
def rate_movie():
    edit_form = EditForm()
    movie_id = request.args.get('id')
    the_movie = db.get_or_404(Movie, movie_id)
    if edit_form.validate_on_submit():
        the_movie.rating = float(edit_form.rating.data)
        the_movie.review = edit_form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", movie=the_movie, form=edit_form)


if __name__ == '__main__':
    app.run(debug=True)
