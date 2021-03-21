import unittest

from dataScienceComponents.classification.Classifier import Classifier


class TestClassifier(unittest.TestCase):

    def setUp(self):
        pass

    def test_strings_a(self):
        c = Classifier()
        cleaned_query = c.get_query_keywords("What are the laws related to human rights?")
        print(cleaned_query)
        self.assertEqual(cleaned_query, 'be laws relate human right')


if __name__ == '__main__':
    unittest.main()
