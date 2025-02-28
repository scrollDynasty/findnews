import unittest
from src.main import get_news, search_web

class TestMain(unittest.TestCase):

    def test_get_news(self):
        # Test the get_news function with a sample query
        articles = get_news("Python")
        self.assertIsInstance(articles, list)
        if articles:
            self.assertIn("title", articles[0])
            self.assertIn("url", articles[0])

    def test_search_web(self):
        # Test the search_web function with a sample query
        results = search_web("Python programming")
        self.assertIsInstance(results, list)
        if results:
            self.assertIn("title", results[0])
            self.assertIn("link", results[0])

if __name__ == "__main__":
    unittest.main()