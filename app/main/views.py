# import render template function
from flask import render_template,request,redirect,url_for
from .forms import ReviewForm
# Import main instance
from ..models import Review
from . import main
# Import functions
from ..request import get_movies,get_movie, search_movie
CATEGORY_LIST=["popular"]
# Generate view functions

@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular movie
    popular_movies = get_movies(CATEGORY_LIST[0])

    title = 'Home - Welcome to The best Movie Review Website Online'

    movie_search = request.args.get('movie_query')

    if movie_search:
        return redirect(url_for('.search',movie_name=movie_search))
    else:
        return render_template('index.html', title = title, popular = popular_movies)

@main.route('/movie/<movie_id>')
def movie(movie_id):
    '''
    Movie view function to display details of a particular movie
    Args:
        1. movie_id:The unique id of the movie being displayed
    '''
    movie_request = get_movie(movie_id)
    reviews = Review.get_reviews(movie_request.movie_id)

    if movie_request:
        title = f'Movie {movie_id}'
        return render_template('movie.html',id=movie_id,title=title,movie=movie_request, reviews=reviews)
    else:
        return render_template('404.html')
@main.route('/search/<movie_name>')
def search(movie_name):
    '''
    View function to display the search results
    '''
    movie_name_list = movie_name.split(" ")
    movie_name_format = "+".join(movie_name_list)
    searched_movies = search_movie(movie_name_format)
    title = f'search results for {movie_name}'

    
    return render_template('search.html',movies = searched_movies)

@main.route('/movie/review/new/<int:id>', methods = ['GET','POST'])
def new_review(id):
    form = ReviewForm()
    movie = get_movie(id)
    
    if movie:
        if form.validate_on_submit():
            title = form.title.data
            review = form.review.data
            new_review = Review(movie.movie_id, title,movie.movie_image, review)
            new_review.save_review()
            return redirect(url_for('.movie',movie_id = movie.movie_id ))

        title = f'{movie.movie_title} review'
        return render_template('new_review.html',title = title, review_form=form, movie=movie)
    else:
        return render_template('404.html')
