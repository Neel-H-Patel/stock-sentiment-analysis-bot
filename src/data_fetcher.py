from config import NEWS_API_KEY
from newsapi import NewsApiClient

news_api = NewsApiClient(api_key=NEWS_API_KEY)

def fetch_news(stock):
    all_related_articles = news_api.get_everything(q=stock, sort_by='publishedAt')
    if all_related_articles['status'] == 'ok':
        if 'articles' in all_related_articles:
            return all_related_articles['articles']
        else:
            print(f'No articles found for {stock}')
            return []
    else:
        print(f'Failed to reach news for {stock}.')
        return []


def fetch_news_for_stocks(stocks):
    stock_news = {}
    for stock in stocks:
        stock_news[stock] = fetch_news(stock)
    return stock_news