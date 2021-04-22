Components are developed individually and integrated together in the next phrase, integration 
## Database 
A relational database is created to store and maintain the relationship between legislations, its pieces and categories. 

## Data Science

### Classification 
Data is analyzed, and split into train and test sets.
Popular multi class textual classification models, Logistic Regression, Random forest SVM, Knearest neighbor are trained and compared to select the best model. 

### Extraction
Document ranking model is implemented using gensim. Models needed for this process (tf-idf model) is created and pickled.
### Simplification
#### lexical model  
CWI model -Implemented with zipf to identify the complex words
Bert model- Generate candidate words to replace the identified complex word
#### Syntactic model 
Identify lengthy compound sentences  
Parse tress are generated to check the grammatical correctness of the split sentences.
 
## Frontend 
Web application created using react 
