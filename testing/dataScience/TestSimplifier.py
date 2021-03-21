import unittest

from dataScienceComponents.Simplifier import Simplifier

class TestClassifier(unittest.TestCase):

    def setUp(self):
        pass

    def test_remove_punctuation(self):
        s=Simplifier()
        removed_punc=s.remove_punctuation(" Any person desirous of being authorized to adopt a child may make application to the court in the manner provided by rules made under section 13, and upon such application being made, the court may, subject to the provisions of this Part, make an order (hereinafter referred to as an “adoption order”) authorizing that person to adopt the child.")
        print(removed_punc)
        self.assertEqual(removed_punc,"Any person desirous of being authorized to adopt a child may make application to the court in the manner provided by rules made under section  and upon such application being made the court may subject to the provisions of this Part make an order hereinafter referred to as an adoption order authorizing that person to adopt the child")

    # def test_cleaned_word(self):
    #
    #     print()
    #     self.assertEqual()


if __name__ == '__main__':
    unittest.main()
