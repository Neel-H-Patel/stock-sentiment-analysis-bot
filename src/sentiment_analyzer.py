from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity

def analyze_stock_sentiment(stock_news):
    stock_sentiment = {}
    for stock, articles in stock_news.items():
        sentiments = [analyze_sentiment(article['title']) for article in articles]
        stock_sentiment[stock] = sum(sentiments) / len(sentiments) if sentiments else 0
    return stock_sentiment