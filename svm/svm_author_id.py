#!/usr/bin/python

""" 
    this is the code to accompany the Lesson 2 (SVM) mini-project

    use an SVM to identify emails from the Enron corpus by their authors
    
    Sara has label 0
    Chris has label 1

"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels

features_train, features_test, labels_train, labels_test = preprocess()

# features_train = features_train[:1*len(features_train)/100]
# labels_train = labels_train[:1*len(labels_train)/100]

#########################################################
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

clf = SVC(kernel='rbf', C=10000)

t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"

t1 = time()
pred = clf.predict(features_test)
print "prediction time:", round(time()-t1, 3), "s"

acc = accuracy_score(pred, labels_test)
print acc

print 'prediction of 10th element:',
print pred[10]

print 'prediction of 26th element:',
print pred[26]

print 'prediction of 50th element:',
print pred[50]

print 'There are ' + str(sum(pred)) + ' emails sent by Chris.'


#########################################################


