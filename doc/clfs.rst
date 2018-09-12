import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import pickle

class clfs:



   def __init__(self):
      """
      Declares two objects used for tracking the location of the
      class classifier for a NGC phrase.

      :Param: self class.
      :Returns: Nothing.
      """
      self.__filename_ngc_clf = '../files/ngc_clf.tr'
      self.__fileobject_ngc_clf = open(self.__filename_ngc_clf, 'wb')



   def train_ngc(self):
      """
      Using the csv file which contains the phrases and the class
      in columns, trains a Multinomial Naive Bayes classifier. Once the
      classifiers is trained, it is dumped into files folder to later
      use.

      :Param: self class.
      :Returns: nothing.
      """
      dataset = pd.read_csv('../files/training.csv', delimiter=',',
         header=None, names=['phrase', 'target'])
      print(dataset)
      text_clf = Pipeline([('vect', CountVectorizer()),
         ('tfidf', TfidfTransformer()),
         ('clf', MultinomialNB()),])
      text_clf.fit(dataset['phrase'], dataset['target'])
      pickle.dump(text_clf, self.__fileobject_ngc_clf)
      


   def get_clf_ngc(self):
      """
      Loads the ngc classifier and returns it.

      :Param: self class.
      :Returns: NGC Multinomial Naive Bayes classifier.
      """
      clf = pickle.load(self.__fileobject_ngc_clf)
      return clf



   def predicText(self, text):
      """
      Predict the text received by parameter into one of three categories:
      abstract, observation or structure.

      :Param: self class and text to predict.
      :Returns: Predicted category as text.
      """
      clf = self.get_clf_ngc()
      result = clf.predict(text)
      return result[0]
