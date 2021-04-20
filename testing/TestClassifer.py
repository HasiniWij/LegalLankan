import unittest

from dataScienceComponents.classification.Classifier import Classifier


class TestClassifier(unittest.TestCase):

    def setUp(self):
        pass

    def test_get_query_keywords(self):
        c = Classifier("../dataScienceComponents/classification/models/svm.pickle","../dataScienceComponents/classification/models/tfidf.pickle")
        cleaned_query = c.get_query_keywords("What are the laws related to human rights?")
        print(cleaned_query)
        self.assertEqual(cleaned_query, 'be laws relate human right')

    def test_create_features_from_df(self):
        c = Classifier("../dataScienceComponents/classification/models/svm.pickle","../dataScienceComponents/classification/models/tfidf.pickle")

        category = c.get_category_of_text("be laws relate human right")
        print(category)
        self.assertEqual(category, 'rights')


if __name__ == '__main__':
    unittest.main()
