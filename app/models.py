class Movie:

    def __init__(self,id,title,overview,image,vote_average,vote_count):

        '''
        Init method that allows us to create instace of the class
        Args:
            1. Title - The name of the movie
            2. Overview - A short description on the movie
            3. image- The poster image for the movie
            4. vote_average - Average rating of the movie
            5. vote_count - How many people have rated the movie
            6. id - The movie id

        '''
        self.movie_id =id
        self.movie_title =title
        self.movie_overview=overview
        self.movie_image ='https://image.tmdb.org/t/p/w500/'+image
        self.movie_vote_average = vote_average
        self.movie_vote_count = vote_count
    
class Review:

    all_reviews = []

    def __init__(self,movie_id,title,imageurl,review):
        self.movie_id = movie_id
        self.title = title
        self.imageurl = imageurl
        self.review = review


    def save_review(self):
        Review.all_reviews.append(self)


    @classmethod
    def clear_reviews(cls):
        Review.all_reviews.clear()
        
    @classmethod
    def get_reviews(cls,id):

        response = []

        for review in cls.all_reviews:
            if review.movie_id == id:
                response.append(review)

        return response