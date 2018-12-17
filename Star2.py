import feedparser
import json
from random import randint
from bottle import route, run, static_file

feed = feedparser.parse('https://www.dailymail.co.uk/articles.rss')


@route('/')
def app():
    return static_file("Star2.html", root="")


@route('/Article')
def headline():
    headlines = []
    r = randint(0, len(feed["entries"])-10)
    for i in range(r, r + 10):
        title = feed["entries"][i]["title"]
        link = "<a href=" + feed["entries"][i]["link"] + ">Go to the article</a>"
        headlines.append({"title": title, "link": link})
    return json.dumps(headlines)


def main():
    run(host='localhost', port=7000)


if __name__ == '__main__':
    main()
