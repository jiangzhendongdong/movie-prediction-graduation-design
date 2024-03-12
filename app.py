from flask import Flask, request, render_template
# request是请求前端数据相关的包，render_template是路由映射相关的包
from flask_migrate import Migrate  # 数据库迁移相关的包
import config  # 数据库连接相关
from crawler import movieLists
from datasql.getPaginated import get_paginated_results
from exts import db  # 导入数据库对象
from models import Movie, PreMovies  # 导入建立的检索表
# from prediction.DoubanPrediction import get_prediction_result
from datasql.checkMovieExists import check_movie_exists
from prediction.DoubanPrediction import get_prediction_result

app = Flask(__name__, template_folder='./templates')
app.config.from_object(config)

# 把app绑定到db上
db.init_app(app)
migrate = Migrate(app, db)


@app.route('/index.html', methods=["POST", "GET"])
def index():
    return render_template('index.html')


@app.route('/moviePrediction.html', methods=["POST", "GET"])
def get_detail():
    global exist, notexist
    key_words = ""
    pre_movies = ""
    exist = ""
    notexist = ""  # 添加这行代码来初始化全局变量notexist
    if request.args.get('key_word', None) is None:
        print("未传参")
        return render_template("moviePrediction.html")
    else:
        key_words = request.args.get('key_word')
        if check_movie_exists(key_words):
            exist = "<<<" + key_words + ">>>" + "电影存在,返回已存储电影数据"
        else:
            notexist = "<<<" + key_words + ">>>" + "电影不存在，准备启动爬虫爬取最新电影数据"

        # 查询PreMovies表中观众从多到少排序的前20条数据
        pre_movies = PreMovies.query.order_by(PreMovies.audience.desc()).limit(10)

        # 使用模糊搜索查询数据库中符合条件的电影条目
        key_words = Movie.query.filter(Movie.movie.like("%{}%".format(key_words))).all()
        print(key_words)

        # 获取分页参数
        page = int(request.args.get('page', 1))
        page_size = int(request.args.get('page_size', 10))

        # 分页查询
        items, item_count, page_count = get_paginated_results(
            Movie.query.filter(Movie.movie.like("%{}%".format(key_words))), page, page_size)

        movie_list = movieLists.movie_list

        # prediction_results = get_prediction_result()
        # data = "随机森林预测评分为： " + str(prediction_results)

        # + "--------" + "xgbboost预测评分为： " + str(prediction_results[-2])
        # + "--------" + "catboost预测评分为： " + str(round(prediction_results[-1], 3))
        # + "--------" + "lgbm预测评分为： " + str(prediction_results[-4])
        # 映射到类似与百度百科的页面，并将查询到的条目传过去

        return render_template("moviePrediction.html", pre_movies=pre_movies, key_words=key_words, exist=exist,
                               notexist=notexist, movies=movie_list)


@app.route('/hotMovies.html', methods=["POST", "GET"])
def hot_movies():
    return render_template('hotMovies.html')


@app.route('/unreleasedFilms.html', methods=["POST", "GET"])
def gonggao():
    movie_list = movieLists.movie_list
    return render_template('unreleasedFilms.html', movies=movie_list)


if __name__ == '__main__':
    app.run()
