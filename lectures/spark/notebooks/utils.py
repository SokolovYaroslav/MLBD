from collections import Counter

class Rating:
    def __init__(self, user_id, movie_id, rating, timestamp):
        self.user_id = user_id
        self.movie_id = movie_id
        self.rating = rating
        self.timestamp = timestamp
        

class Movie:
    def __init__(self, movie_id, title, genres):
        self.movie_id = movie_id
        self.title = title
        self.genres = genres
