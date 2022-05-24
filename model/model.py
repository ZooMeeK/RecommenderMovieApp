from component.sqlite import SQLite
from logs.logs import Logs

l = Logs()
s = SQLite('data/movie_data.db')


class Model:
    
    
    def __init__(self):
        pass
        
    
    def add_new_film(self, name, year, genres_list):
        title = '{} ({})'.format(name, year)
        genres = "|".join(genres_list)
        s.new_film(title, genres)


    def get_score_user_movie(self):
        pass        
    
    
    def update_user_score(self, user_id, movie_id, rating):
        s.update_user_film_rating(user_id, movie_id, rating)
        
        
    def add_user_score(self, user_id, movie_id, rating):
        s.new_user_film_rating(user_id, movie_id, rating)