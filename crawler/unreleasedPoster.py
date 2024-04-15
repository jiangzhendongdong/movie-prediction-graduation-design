import pymysql

# 连接到数据库
conn = pymysql.connect(host='localhost', port=3306, user='root', password='123456', db='douban')

cursor = conn.cursor()

# 查询最新的电影数据
query = "SELECT * FROM images ORDER BY id ASC LIMIT 9"
cursor.execute(query)
images = cursor.fetchall()

# 生成HTML代码
html_code = ""
image_list = []

for image in images:
    poster_data = image[1]
    poster_name = image[2]
    # movie_img = movie[2]

    image_dict = {
        "data": poster_data,
        "name": poster_name
    }

    image_list.append(image_dict)

# 输出HTML代码或将其发送到前端
print(image_list)

# 关闭数据库连接
cursor.close()
conn.close()
