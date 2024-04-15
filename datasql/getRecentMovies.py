import json

import pymysql


def getRecentMovies():
    # 连接到数据库
    connection = pymysql.connect(host='localhost', user='root', password='123456', db='douban')
    cursor = connection.cursor()
    cursor.execute(
        "SELECT year, COUNT(*) as movie_count FROM douban_moviesdata WHERE year >= YEAR(NOW()) - 14 GROUP BY year ORDER BY year;")
    data = cursor.fetchall()
    years = [row[0] for row in data]
    movie_counts = [row[1] for row in data]
    data_json = {"years": years, "movie_counts": movie_counts}
    json_str = json.dumps(data_json)
    print(json_str)
    return json_str


