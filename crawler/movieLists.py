import pymysql

# 连接到数据库
conn = pymysql.connect(host='localhost', port=3306, user='root', password='123456', db='douban')

cursor = conn.cursor()

# 查询最新的电影数据
query = "SELECT * FROM pre_movies ORDER BY id ASC LIMIT 9"
cursor.execute(query)
movies = cursor.fetchall()

# 生成HTML代码
html_code = ""
movie_list = []

for movie in movies:
    movie_url = movie[3]
    movie_title = movie[2]
    # movie_img = movie[2]

    movie_dict = {
        "url": movie_url,
        "title": movie_title
    }

    movie_list.append(movie_dict)

# 输出HTML代码或将其发送到前端
print(movie_list)

# 关闭数据库连接
cursor.close()
conn.close()
