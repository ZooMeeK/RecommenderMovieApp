from component.sqlite_core import SQLiteCore
from logs.logs import Logs
import datetime
l = Logs()


class SQLite(SQLiteCore):
    
    def __init__(self, db_location):
        self.db_location = db_location
    
    
    def select_user_film_rating(self, user_id, movie_id):
        
        query = 'SELECT rating FROM ratings WHERE userId = {} AND movieId = {}'.format(user_id, movie_id)
        result = self.select(query)[0][0]
        l.write_logs('Get rating user_id {} by movie_id {}, rating {}'.format(user_id, movie_id, result))
        
        return result
    
    
    def get_all_ratings_data(self):
        
        query = 'SELECT userId, movieId, rating FROM ratings'
        result = self.select(query)
        l.write_logs('Get all ratings data')
        
        return result
    
    
    def get_movie_names(self, movie_id):
        
        query = 'SELECT title FROM movies WHERE movieId = {}'.format(movie_id)
        result = self.select(query)
        l.write_logs('Get movie names for movie_id {}'.format(movie_id))
        
        return result
    
    
    def new_user_film_rating(self, user_id, movie_id, rating):
        
        timestamp = int(datetime.datetime.utcnow().timestamp())
        query = 'INSERT INTO ratings (userId, movieId, rating, timestamp) VALUES ({},{},{},{})'.format(user_id, movie_id, rating, timestamp)
        self.update(query)
        l.write_logs('User_id {} insert rating {} for movie_id {}'.format(user_id, rating, movie_id))
        
        
    def update_user_film_rating(self, user_id, movie_id, rating):
        
        timestamp = int(datetime.datetime.utcnow().timestamp())
        query = 'UPDATE ratings SET rating = {}, timestamp = {} WHERE userId = {} AND movieId = {}'.format(rating, timestamp, user_id, movie_id)
        self.insert(query)
        l.write_logs('User_id {} update rating {} for movie_id {}'.format(user_id, rating, movie_id))
        

    def new_film(self, title, genre):
        
        movie_id = self.get_new_movie_id()
        query = 'INSERT INTO movies (movieId, title, genres) VALUES ("{}","{}","{}")'.format(movie_id, title, genre)
        self.insert(query)
        l.write_logs('Add folm {} by movie_id {}'.format(title, movie_id))  
        
    def get_new_movie_id(self):
        
        query = 'SELECT MAX(movieId) FROM movies'
        result = self.select(query)[0][0] + 1
        l.write_logs('Create new movie_id {}'.format(result))
        
        return result
        
        