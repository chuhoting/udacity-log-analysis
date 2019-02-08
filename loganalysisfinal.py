# Database code for the DB Forum, full solution!

import psycopg2

DBNAME = "news"

request1 = "1. What are the most popular three articles of all time?"
query1 = ("""
        SELECT articles.title, COUNT(*) AS num
        FROM articles
        JOIN log
        ON log.path LIKE concat('/article/%', articles.slug)
        GROUP BY articles.title
        ORDER BY num DESC
        LIMIT 3;
        """)
request2 = "2. Who are the most popular article authors of all time?"
query2=("""select authors.name,
        count (*) as num from authors,
        articles, log where concat('/article/', articles.slug) = log.path AND articles.author = authors.id group
        by authors.name order by num desc;
        """)
request3= "3. On which days did more than 1% of requests lead to errors?"
query3= ("""
        SELECT total.day,
        ROUND(((errors.error_requests*1.0) / total.requests), 3) AS percent
        FROM (
        SELECT date_trunc('day', time) "day", count(*) AS error_requests
        FROM log
        WHERE status LIKE '404%'
        GROUP BY day
        ) AS errors
        JOIN (
        SELECT date_trunc('day', time) "day", count(*) AS requests
        FROM log
        GROUP BY day
        ) AS total
        ON total.day = errors.day
        WHERE (ROUND(((errors.error_requests*1.0) / total.requests), 3) > 0.01)
        ORDER BY percent DESC;
        """)
query4=("""WITH numer as (
        select cast(log.time as date) as day, count(log.status) as num
        from log
        where log.status
        like '404%'
        group by day
        ), denom as(
        select cast(log.time as date) as day, count(log.status) as num
        from log
        group by day
        ), error as(
        select numer.num::float /denom.num::float * 100 as errorpc
        from numer,denom
        where numer.day=denom.day
        )
        select cast(log.time as date),errorpc from error,log where errorpc >1 and log.status like '404%';""")

def getdata(sqlcode):
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(sqlcode)
    posts= c.fetchall()
    db.close()
    return posts

def print_results(q_list):
    for i in range(len(q_list)):
        title = q_list[i][0]
        res = q_list[i][1]
        print("%s - %d" % (title, res) + " views")
    print("\n")

answer1=getdata(query1)
answer2=getdata(query2)
answer3=getdata(query3)
answer4=getdata(query4)
print(request1)
print_results(answer1)
print(request2)
print_results(answer2)
print(request3)
print(answer4[0][0])
print(+answer4[0][1])
