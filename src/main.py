from data_fetcher import fetch_news_for_stocks
from sentiment_analyzer import analyze_stock_sentiment

def main():
    stocks = ['AAPL', 'NVDA', 'GOOGL']
    stock_news = fetch_news_for_stocks(stocks)
    stock_sentiment = analyze_stock_sentiment(stock_news)

    for stock, sentiment in stock_sentiment.items():
        print(f'Stock: {stock}, Sentiment: {sentiment:.2f}')

if __name__ == '__main__':
    main()