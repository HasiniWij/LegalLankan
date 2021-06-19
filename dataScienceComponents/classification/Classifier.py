import pickle  # models are stored as pickles and loaded to this file
import pandas as pd  # features are stored and dealt using dataframes
from nltk.corpus import stopwords  # Stop words are removed
from nltk.stem import WordNetLemmatizer  # Lemmatized to get the words to same format

from dataScienceComponents.extraction.Extractor import Extractor


class Classifier:

    def __init__(self, svm_path, tfidf_path):

        with open(svm_path, 'rb') as data:
            self.model = pickle.load(data)

        with open(tfidf_path, 'rb') as data:
            self.tfidf = pickle.load(data)

        self.category_codes = {
            'crime': 0,
            'family': 1,
            'rights': 2,
            'employment': 3,
            'other': 4
        }



    def create_features_from_df(self, df):

        punctuation_signs = list("?:!.,;")
        stop_words = list(stopwords.words('english'))

        df['Content_Parsed_1'] = df['content'].str.replace("\r", " ")
        df['Content_Parsed_1'] = df['Content_Parsed_1'].str.replace("\n", " ")
        df['Content_Parsed_1'] = df['Content_Parsed_1'].str.replace("    ", " ")
        df['Content_Parsed_1'] = df['Content_Parsed_1'].str.replace('"', '')

        df['Content_Parsed_2'] = df['Content_Parsed_1'].str.lower()

        df['Content_Parsed_3'] = df['Content_Parsed_2']
        for punctuation_sign in punctuation_signs:
            df['Content_Parsed_3'] = df['Content_Parsed_3'].str.replace(punctuation_sign, '')

        df['Content_Parsed_4'] = df['Content_Parsed_3'].str.replace("'s", "")

        wordnet_lemmatizer = WordNetLemmatizer()
        nrows = len(df)
        lemmatized_text_list = []

        for row in range(0, nrows):
            # Create an empty list containing lemmatized words
            lemmatized_list = []
            # Save the text and its words into an object
            text = df.loc[row]['Content_Parsed_4']
            text_words = text.split(" ")
            # Iterate through every word to lemmatize
            for word in text_words:
                lemmatized_list.append(wordnet_lemmatizer.lemmatize(word, pos="v"))
            # Join the list
            lemmatized_text = " ".join(lemmatized_list)
            # Append to the list containing the texts
            lemmatized_text_list.append(lemmatized_text)

        df['Content_Parsed_5'] = lemmatized_text_list

        df['Content_Parsed'] = df['Content_Parsed_5']
        for stop_word in stop_words:
            regex_stop_word = r"\b" + stop_word + r"\b"
            df['Content_Parsed'] = df['Content_Parsed'].str.replace(regex_stop_word, '')

        df = df['Content_Parsed']
        # df = df.rename(columns={'Content_Parsed_6': 'Content_Parsed'})

        # TF-IDF
        features = self.tfidf.transform(df).toarray()
        return features

    def get_category_name(self, category_id):
        for category, id_ in self.category_codes.items():
            if id_ == category_id:
                return category

    def predict_from_features(self, features):
        # Obtain the highest probability of the predictions for each article
        predictions_probability = self.model.predict_proba(features).max(axis=1)

        # Predict using the input model
        predictions_pre = self.model.predict(features)

        # Replace prediction with 6 if associated cond. probability less than threshold
        predictions = []

        for prob, cat in zip(predictions_probability, predictions_pre):

            if prob > .5:
                predictions.append(cat)
            else:
                predictions.append(4)

        # Return result
        categories = [self.get_category_name(x) for x in predictions]
        return categories

    # call this method to get the category of a document or a query
    def get_category_of_text(self, input_text):

        E=Extractor()
        keywords = E.get_query_keywords(input_text)

        content = [keywords]

        query_df = pd.DataFrame(
            {'content': content
             })

        features = self.create_features_from_df(query_df)
        predictions = self.predict_from_features(features)
        return predictions[0]
