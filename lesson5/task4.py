# В файле хранятся данные с сайта IMDB. Скопированные данные
# хранятся в файле ./data_hw5/ ratings.list.
# Откройте и прочитайте файл(если его нет необходимо вывести ошибку).
# Найдите ТОП250 фильмов и извлеките заголовки.
# Программа создает 3 файла  top250_movies.txt – названия файлов,
# ratings.txt – гистограмма рейтингов, years.txt – гистограмма годов.


rating = open("data_hw5/ratings.list", 'r')
rating.close()

import IMDbPY

film = IMDbPY.IMDb()

search = film.get_top250_movies()

for i in range(250):
    print(search[i]['title'])

def movies(*args):
    for i in args:
        movies = open(f"data_hw5/{i}", 'w')
        movies.close()

movies('top250_movies.txt', 'ratings.txt', 'years.txt')