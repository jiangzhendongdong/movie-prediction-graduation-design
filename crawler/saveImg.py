import pymysql
import os
import traceback


def write_pic2mysql(path):
    # """
    # 读取图片写入数据库
    # :param path: 读取的图片的路径
    # :param config: 数据库连接配置信息
    # :return: None
    # """
    # filename = path.split('/')[-1]

    global sql
    path = 'D:\\movie-prediction-graduation-design\\static\\2024\\3月'

    try:
        conn = pymysql.connect(host='localhost',
                               port=3306,
                               user='root',
                               password='123456',
                               db='douban',
                               charset='utf8',
                               use_unicode=True)
        cursor = conn.cursor()

        for filename in os.listdir(path):
            file_path = os.path.join(path, filename)
            try:
                with open(file_path, 'rb') as f:
                    img = f.read()
            except:
                print('读取失败: {}'.format(filename))
                continue
            # 注意一下这里的 {0} 的引号，可以试一下去掉引号会提醒没有者找到该字段
            sql = "INSERT INTO images (data, name) VALUES (%s, '{0}')".format(filename)
            # 设置id为0
            cursor.execute("SET @auto_id = 0;")
            # UPDATE 表名 set id = (@auto_id := @auto_id +1);
            cursor.execute("UPDATE images set id = (@auto_id := @auto_id +1);")
            # # ALTER TABLE 表名 AUTO_INCREMENT = 1;
            cursor.execute("ALTER TABLE images AUTO_INCREMENT = 1;")
            cursor.execute(sql, img)
            conn.commit()

        cursor.close()
        conn.close()
        print('写入 {} 成功'.format(filename))

    except Exception as e:
        print(e)
        print('写入失败')


def read_mysql2pic(path, filename):
    # """
    # 从数据库中读取图片
    # :param path: 你要保存的图片的路径
    # :param filename:你要从数据库读取的名字，在本例子相当于数据库中的name字段
    # :param config: 数据库连接配置信息
    # :return: None
    # """
    try:
        conn = pymysql.connect(host='localhost',
                               port=3306,
                               user='root',
                               password='123456',
                               db='douban',
                               charset='utf8',
                               use_unicode=True)
        cursor = conn.cursor()
        cursor.execute("select data from images where name = '{}'".format(filename))
        res = cursor.fetchone()[0]
        with open(path, 'wb') as f:
            f.write(res)
        print('从数据库中读取 {} 成功'.format(filename))
    except Exception as e:
        print(e)
        print('读取数据库中的图片失败')


if __name__ == '__main__':
    write_pic2mysql('D:\\movie-prediction-graduation-design\\static\\2024\\3月')
    print(' 写入后再读取 '.center(50, '*'))
    # read_mysql2pic('D:\\movie-prediction-graduation-design\\static\\2024\\3月read_挡马夺刀.jpg', '挡马夺刀.jpg')
