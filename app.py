from flask import Flask, render_template
from newsapi import NewsApiClient

app=Flask(__name__)


@app.route('/')
def index():
    newsapi = NewsApiClient(api_key="b9feb067b6924c4db48214cc7dc56dd8")
    topHeadLines = newsapi.get_top_headlines(sources="bbc-news,the-verge")

    articles = topHeadLines['articles']

    desc=[]
    news=[]
    img=[]

    for i in articles:
        news.append(i['title'])
        desc.append(i['description'])
        img.append(i['urlToImage'])


    myList = zip(news, desc, img)

    return render_template('index.html', context=myList)


if __name__ == '__main__':
    app.run(debug=True)


