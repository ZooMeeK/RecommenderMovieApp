from component.sqlite import SQLite
import pandas as pd
from logs.logs import Logs

l = Logs()

user_id = 1
movie_id = 1

s = SQLite('data/movie_data.db')

result = s.new_film('21314421dsddf', '123weqwrqweqwe')
"""
result = s.get_all_ratings_data()

df = pd.DataFrame(result, columns= ['user_id', 'movie_id', 'score'])

df_pivot = pd.pivot_table(df, values = 'score', index = 'user_id', columns = 'movie_id')
df_pivot = df_pivot.fillna(0)

#user_dict = {i:ind for ind, i in enumerate(df['user_id'].unique())}
#movie_dict = {i:ind for ind, i in enumerate(df['movie_id'].unique())}

#user = user_dict[78]
#movie = movie_dict[150]

##print(df_pivot.columns)
#print(user)

def get_users_film_rating(movie_id, user_id):
    
    try:    
        rating = df_pivot[movie_id][user_id]
        movie_name = s.get_movie_names(movie_id)
        result_movie_name = movie_name[0][0].split('(')[0]
        string = 'User {} expects rating {} for film {}'.format(user_id, rating, result_movie_name)
        l.write_logs(string)
    except Exception as e:        
        string = 'User {} expects rating {} for film {}'.format(user_id, 0, 'undefined')
        l.write_logs('Error {}'.format(e))    
    return string
    

    

res1 = get_users_film_rating(29, 0)
#s.update_user_film_rating(700, 700, 706)
'''
блок с магией
'''
print('------------')
res2 = get_users_film_rating(29, 95)



"""