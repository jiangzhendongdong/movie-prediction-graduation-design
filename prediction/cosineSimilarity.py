import pandas as pd
from scipy import spatial
import numpy as np

movies = pd.read_csv("D:\\movie-prediction-graduation-design\\DoubanMoviesData.csv")


# 首先对于每部影片都构造二元数组表示类型、导演和主演
def binary(wordlist0, wordlist):
    binary = []
    for word in wordlist0.index:
        if word in wordlist:
            binary.append(1)
        else:
            binary.append(0)
    return binary


def countN(column):
    count = dict()
    for row in column:
        for ele in row:
            if ele in count:
                count[ele] += 1
            else:
                count[ele] = 1
    return count


def angle(movie1, movie2):
    dis = 0
    dis_tot = 0
    iterlist = [[movie1.genres_bin, movie2.genres_bin],
                [movie1.director_bin, movie2.director_bin],
                [movie1.actors_bin, movie2.actors_bin]]
    for b1, b2 in iterlist:
        if (1 not in b1) or (1 not in b2):
            dis_tot = 1
        else:
            dis = spatial.distance.cosine(b1, b2)
        dis_tot += dis
    return dis_tot


genres = pd.Series(countN(movies.genres)).sort_values()
movies['genres_bin'] = [binary(genres, x) for x in movies.genres]  # 影片类型二元数组
directors = movies.groupby('directors').size().sort_values(ascending=False)
movies['director_bin'] = [binary(directors, x) for x in movies.directors]  # 影片导演二元数组
actors = pd.Series(countN(movies.actors.sort_values(ascending=False)))
movies['actors_bin'] = [binary(actors, x) for x in movies.actors]  # 影片主演二元数组


def predictor(new_movie):
    movie_bin = pd.Series()
    movie_bin['genres_bin'] = binary(genres, new_movie['genres'])
    movie_bin['director_bin'] = binary(directors, new_movie['directors'])
    movie_bin['actors_bin'] = binary(actors, new_movie['actors'])
    vote = movies.copy()
    vote['angle'] = [angle(vote.iloc[i], movie_bin) for i in range(len(vote))]
    vote_avg1 = np.mean(vote.douban_score[0:1000])
    vote_avg2 = np.mean(vote.douban_score[2000:3000])
    vote_avg3 = np.mean(vote.douban_score[4000:5000])
    vote_avg4 = np.mean(vote.douban_score[6000:7000])
    vote_avg5 = np.mean(vote.douban_score[8000:9000])
    vote_avg = np.mean([vote_avg1, vote_avg2, vote_avg3, vote_avg4 ,vote_avg5])
    return vote_avg


# 测试
release_movie = {'genres': ['喜剧', '爱情'],
                 'directors': ['陈咏燊'],
                 'actors': ['黄子华', '邓丽欣', '张继聪', '王菀之']}

print(predictor(release_movie))
