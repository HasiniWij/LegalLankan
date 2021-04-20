import unittest

from dataScienceComponents.classification.Classifier import Classifier
from dataScienceComponents.extraction.Extractor import Extractor


class TestExtractor(unittest.TestCase):

    def setUp(self):
        pass

    def test_strings_a(self):
        c = Classifier("../../dataScienceComponents/classification/models/svm.pickle",
                       "../../dataScienceComponents/classification/models/tfidf.pickle")

        query = "What are the main laws related to human rights?"

        category = c.get_category_of_text(query)
        keywords = c.get_query_keywords(query)
        e = Extractor(category)
        piece_indexes = e.get_ranked_documents(keywords)
        self.assertEqual(len(piece_indexes), 5)


if __name__ == '__main__':
    unittest.main()