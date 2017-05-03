import json, requests, pickle, os
from flask import Flask, render_template
app = Flask(__name__)

API_KEY = os.environ['NEWS_API_KEY'] # get yours at https://newsapi.org
NEWS_SOURCE='daily-mail'


@app.route('/')
def hello_world():
    return render_template('index.html',
                           news=news_articles())

def clickbait_label(text):
    CLASSIFIER_DIR = "../classifiers/clickbait_svc_v1"
    with open(CLASSIFIER_DIR, 'rb') as f:
        classifier = pickle.load(f)
    return classifier.predict([text])[0]

def news_articles():
    r = requests.get(
        'https://newsapi.org/v1/articles?source={}'
        '&sortBy=latest&apiKey={}'.format(NEWS_SOURCE, API_KEY)
    )
    if r.status_code == 200:
        articles = r.json()['articles']
        for article in articles:
            article['clickbait'] = clickbait_label(article['title'] + article['description'])
        news = {
            'source': NEWS_SOURCE,
            'articles': articles
        }
        return news
    else:
        return None
