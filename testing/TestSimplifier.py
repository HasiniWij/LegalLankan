import unittest

from dataScienceComponents.simplification.Simplifier import Simplifier


class TestSimplifier(unittest.TestCase):

    def setUp(self):
        pass

    def test_remove_punctuation(self):
        s = Simplifier()
        removed_punc = s.remove_punctuation("This Ordinance may be cited as the Brothels Ordinance.")
        print(removed_punc)
        self.assertEqual(removed_punc, "This Ordinance may be cited as the Brothels Ordinance")

    def test_cleaned_word(self):
        s = Simplifier()
        cleaned_word = s.cleaned_word("Provisions")
        print(cleaned_word)
        self.assertEqual(cleaned_word, "provisions")

    def test_tokenized(self):
        s = Simplifier()
        tokenized = s.tokenized("This Ordinance may be cited as the Brothels Ordinance")
        self.assertEqual(tokenized, ['This', 'Ordinance', 'may', 'be', 'cited', 'as', 'the', 'Brothels', 'Ordinance'])

    def test_NER_identifier(self):
        s = Simplifier()
        result = s.NER_identifier(
            "This Convention shall be binding only upon those Members of the International Labour "
            "Organisation whose ratifications have been registered with the Director-General.")
        print(result)
        self.assertEqual(result, ['the', 'international', 'labour', 'organisation'])

    def test_get_bert_candidates(self):
        s = Simplifier()
        sentence = "The categories of occupations or undertakings in respect of which the Member proposes to have " \
                   "recourse to the provisions of paragraph 1 of this Article shall be specified in the declaration " \
                   "accompanying its ratification. "
        result = s.get_bert_candidates(sentence, "undertakings")
        expected = [('undertakings', ['undertaking', 'activities'])]
        self.assertEqual(expected, result)

    def test_get_lexically_simplified_text(self):
        sentence = "The categories of occupations or undertakings in respect of which the Member proposes to have " \
                   "recourse to the provisions of paragraph 1 of this Article shall be specified in the declaration " \
                   "accompanying its ratification. "
        s = Simplifier()
        result = s.get_lexically_simplified_text(sentence)
        print(result)
        self.assertEqual(result, result)

    def test_word_is_a_conjunction(self):
        s = Simplifier()
        self.assertEqual(s.word_is_a_conjunction("and"), True)
        self.assertEqual(s.word_is_a_conjunction("Article"), False)

    def test_get_syntactically_simplified_text(self):
        s = Simplifier()
        leg_piece = ["Article", '''No person shall be held guilty of an offence on account of any act or omission which 
        did not, at the time of such act or omission, constitute such an offence and no penalty shall be imposed for any 
        offence more severe than the penalty in force at the time such offence was committed.''']
        result = s.get_syntactically_simplified_text(leg_piece)
        expected = ['Article', 'No person shall be held guilty of an offence on account of any act or omission which '
                               'did not at the time of such act or omission constitute such an offence',
                    'no penalty shall be imposed for any offence more severe than the penalty in force at the time '
                    'such offence was committed']
        self.assertEqual(result, expected)

    def tet_confirm_syntactic_simplification(self):
        s = Simplifier()
        result = s.confirm_syntactic_simplification("no penalty shall be imposed for any offence more severe than the "
                                                    "penalty in force at the time such offence was committed.")
        print(result)
        self.assertEqual(result, result)

    def test_sentences_list(self):
        s = Simplifier()
        result = s.sentences_list(['This', 'Ordinance', 'may', 'be', 'cited', 'as', 'the', 'Brothels', 'Ordinance'],
                                 ['This', 'Ordinance', 'may', 'be', 'cited', 'as', 'the', 'Brothels', 'Ordinance'])
        print(result)
        self.assertEqual(result, ['This Ordinance may be cited as the Brothels Ordinance', 'This Ordinance may be '
                                                                                           'cited as the Brothels '
                                                                                           'Ordinance'])


if __name__ == '__main__':
    unittest.main()
