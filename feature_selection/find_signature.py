#!/usr/bin/python

import pickle
import numpy
numpy.random.seed(42)
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import TfidfVectorizer


### the words (features) and authors (labels), already largely processed
### these files should have been created from the previous (Lesson 10) mini-project.
words_file = "../text_learning/your_word_data.pkl" 
authors_file = "../text_learning/your_email_authors.pkl"
word_data = pickle.load( open(words_file, "r"))
authors = pickle.load( open(authors_file, "r") )



### test_size is the percentage of events assigned to the test set (remainder go into training)
### feature matrices changed to dense representations for compatibility with classifier
### functions in versions 0.15.2 and earlier
from sklearn import cross_validation
features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(word_data, authors, test_size=0.1, random_state=42)

from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5,
                             stop_words='english')
features_train = vectorizer.fit_transform(features_train)
features_test  = vectorizer.transform(features_test).toarray()


### a classic way to overfit is to use a small number
### of data points and a large number of features
### train on only 150 events to put ourselves in this regime
features_train = features_train[:150].toarray()
labels_train   = labels_train[:150]

clf = DecisionTreeClassifier()
clf.fit(features_train, labels_train)

pred = clf.predict(features_test)
acc = accuracy_score(pred, labels_test)

print "\nAccuracy of decision tree:",
print acc

number_of_important_features = 0
most_important_coef = None
for i in clf.feature_importances_:
	if i > 0.2:
		most_important_coef = i
		number_of_important_features += 1

print "\nMost important feature has coeff of",
print round(most_important_coef, 3),
print "and has index of",
max_index = numpy.nanargmax(clf.feature_importances_)
print max_index

print "\nMost important feature word:",

# vectorizer.fit_transform(word_data)
vocab_list = vectorizer.get_feature_names()

print vocab_list[max_index]

print "\nNumber of important features:",
print number_of_important_features




