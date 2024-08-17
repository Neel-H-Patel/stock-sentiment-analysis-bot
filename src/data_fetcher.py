from config import NEWS_API_KEY
from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key=NEWS_API_KEY)

def fetch_news(stock):
    all_related_articles = newsapi.get_everything(q=stock, sort_by='publishedAt')
    return all_related_articles['articles']

def fetch_news_for_stocks(stocks):
    stock_news = {}
    for stock in stocks:
        stock_news[stock] = fetch_news(stock)
    return stock_news