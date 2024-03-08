import requests
import os


def download_covers(subjects):
    for subject in subjects:
        cover_url = subject['cover']
        title = subject['title']

        try:
            response = requests.get(cover_url)
            response.raise_for_status()

            # 设置保存路径和文件名
            save_path = 'D:\\movie-prediction-graduation-design\\static\\download-movies-image'
            filename = save_path + title + '.jpg'

            with open(filename, 'wb') as f:
                f.write(response.content)

            print(f"成功下载并保存电影《{title}》的海报图")
        except Exception as e:
            print(f"下载电影《{title}》的海报图失败：{e}")


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 "
                  "Safari/537.36"
}
cookies = {
    'Cookie': 'll="108288"; bid=up0rofOlT4o; __yadk_uid=6Piu6D9gQlgkP4gC3hgArFi0RunP6k5T; push_noty_num=0; '
              'push_doumail_num=0; _vwo_uuid_v2=DDF215CC01DBBE41F222EC90538FB2D8A|49272204d8258e96190df0b4354e4dd2; '
              '__utma=30149280.1436538775.1618204010.1618204010.1618721534.2; '
              '__utmz=30149280.1618721534.2.2.utmcsr=qdan.me|utmccn=(not set)|utmcmd=(not set)|utmctr=(not provided); '
              '__utma=223695111.1097268048.1618204010.1618204010.1618721534.2; '
              '__utmz=223695111.1618721534.2.2.utmcsr=qdan.me|utmccn=(not set)|utmcmd=(not set)|utmctr=(not '
              'provided); _pk_ref.100001.4cf6=["","",1619498308,"https://m.douban.com/"]; _pk_ses.100001.4cf6=*; '
              '__gads=ID=711c888999a2e5f0-22dfaadf9dc7003c:T=1619498309:RT=1619498309:S'
              '=ALNI_MZFOiKjGCpwqqIx_9KalMsBejTvlA; '
              '_pk_id.100001.4cf6=144675c5bcfcfa6a.1618198911.4.1619498357.1618722649.; dbcl2="226186082:B5H3Q7prE2E"'
}
url = ("https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20"
       "&page_start=")

response = requests.get(url,headers=headers,cookies=cookies)
data = response.json()

if 'subjects' in data:
    subjects = data['subjects']
    download_covers(subjects)
else:
    print("获取电影数据失败")
