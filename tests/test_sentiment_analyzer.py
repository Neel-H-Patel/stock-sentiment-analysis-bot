import unittest
from src.sentiment_analyzer import analyze_sentiment

class TestSentimentAnalyzer(unittest.TestCase):
    def test_analyze_sentiment(self):
        self.assertAlmostEqual(analyze_sentiment("Good product"), 0.7, places=1)
        self.assertAlmostEqual(analyze_sentiment("Bad experience"), -0.7, places=1)

if __name__ == '__main__':
    unittest.main()