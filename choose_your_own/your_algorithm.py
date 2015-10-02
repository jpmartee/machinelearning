#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow" points mixed
### in together--separate them so we can give them different colors in the scatterplot,
### and visually identify them
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()
#################################################################################

### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary

#clf = AdaBoostClassifier(algorithm='SAMME')
#clf = clf.fit(features_train, labels_train)
#pred_ab = clf.predict(features_test)
#acc_ab = accuracy_score(pred_ab, labels_test)

#clf_rf = RandomForestClassifier(min_samples_split=50)
#clf_rf = clf_rf.fit(features_train, labels_train)
#pred_rf = clf_rf.predict(features_test)
#acc_rf = accuracy_score(pred_rf, labels_test)

clf_kn = KNeighborsClassifier(n_neighbors=8)
clf_kn = clf_kn.fit(features_train, labels_train)
pred_kn = clf_kn.predict(features_test)
acc_kn = accuracy_score(pred_kn, labels_test)

#print 'AdaBoost acc: ' + str(acc_ab)
#print 'RandomForest acc: ' + str(acc_rf)
print 'KNN acc: ' + str(acc_kn)


try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass
