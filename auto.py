import pymysql

# 连接到数据库
conn = pymysql.connect(host='localhost', port=3306, user='root', password='123456',
                       db='云南电网公司')
cur = conn.cursor()

# 替换关键词的列表
keywords = ["昆明供电局", "曲靖供电局", "红河供电局", "大理供电局", "昭通供电局", "玉溪供电局",
            "云南电网专职驾驶员（外协）", "普洱供电局", "楚雄供电局", "文山供电局", "临沧供电局", "云电投控",
            "送变电工程公司", "丽江供电局", "公司本部", "西双版纳供电局", "德宏供电局", "怒江供电局", "迪庆供电局",
            "信息中心", "试验研究院（集团）", "统调电厂", "保山供电局", "电力科学研究院", "瑞丽供电局",
            "电力建设监理咨询公司", "培训与评价中心", "输电分公司", "云网能源投资公司", "建设分公司",
            "昆明电力交易中心", "中共云南电网公司党校", "省电力行业协会", "云南省电机工程学会", "云电投控；南方电网",
            "电力交易中心"]

# 循环替换关键词并执行SQL语句
for keyword in keywords:
    create_table_sql = f"CREATE TABLE {keyword} AS SELECT * FROM 云南电网公司 WHERE f3 LIKE '%{keyword}%'"
    cur.execute(create_table_sql)

# 关闭连接
cur.close()
conn.close()
print('亲爱的小主 已全部执行完毕！！！')
