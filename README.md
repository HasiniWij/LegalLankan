# LegalLankan
### A web application that makes law accessible and understandable to the general public of Sri Lanka.

## Frontend
React is used to build the UI of the web application.

## Backend 
Flask library is used in building the API of this project.

## Data Science Components
Includes components which makes use of multiple ML and NLP techniques.

### Multi-class Text Classification
Sci-kit Learn is used to implement Support Vector Classification to classify uploaded law documents into 4 classes, namely crime, family, rights and employement. 

### Document Similarity
Gensim and jieba libraries are used to calculate document similarities used in the Answer Extraction module.

### Text Simplification
Zipf frequency and pre-trained BERT model are used for complex word identification and in finding candidates for complex words respectively, in the Lexical Simplification model along with spacy for NER.
Stanford CoreNLP is used to generate parse trees for Syntactic Simplification.

NLTK has been used for text preprocessing tasks and some other libraries utilized include Pandas, Pickle and wordfreq.


