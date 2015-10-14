 #!/usr/bin/python

""" 
    starter code for exploring the Enron dataset (emails + finances) 
    loads up the dataset (pickled dict of dicts)

    the dataset has the form
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person
    you should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""
import sys
import pickle

sys.path.insert(0, '../tools/')

from feature_format import *

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
#remove TOTAL from enron_data
enron_data.pop('TOTAL')

people_in_dataset = len(enron_data)

print 'no. people in dataset:', len(enron_data)
for person in enron_data:
    print person

print '\nno. of features:', len(enron_data['METTS MARK'])
for feature in enron_data['METTS MARK']:
    print feature

poi = 0
for i in enron_data:
    if enron_data[i]['poi'] == True:
        poi += 1

# print enron_data.keys()

print "\nno. of poi's:", poi
for i in enron_data:
    if enron_data[i]['poi'] == True:
        print i

# print "Value of stock belonging to James Prentice:",
# print enron_data['PRENTICE JAMES']['total_stock_value']

# print 'Emails from Wesley Colwell to persons of interest:',
# print enron_data['COLWELL WESLEY']['from_this_person_to_poi']

# print'Value of stock options exercised by Jeffrey Skilling:',
# print enron_data['SKILLING JEFFREY K']['exercised_stock_options']

# print "Value of stock belonging to Jeffrey Skilling:",
# print enron_data['SKILLING JEFFREY K']['total_payments']

# print "Value of stock belonging to Kenneth Lay:",
# print enron_data['LAY KENNETH L']['total_payments']

# print "Value of stock belonging to Andrew Fastow:",
# print enron_data['FASTOW ANDREW S']['total_payments']

features_with_missing_values = []
for person, feature in ((person, feature) for person in enron_data for feature in enron_data['METTS MARK']):
    if enron_data[person][feature] == 'NaN' and feature not in features_with_missing_values:
        features_with_missing_values.append(feature)

print '\nNo. of features with missing values:', len(features_with_missing_values)
print 'Features with missing values:' 
for feature in features_with_missing_values:
    print feature

no_listed_salary = 0
for i in enron_data:
    if enron_data[i]['salary'] == 'NaN':
        no_listed_salary += 1

no_known_email = 0
for i in enron_data:
    if enron_data[i]['email_address'] == 'NaN':
        no_known_email += 1

quantified_salaries = people_in_dataset - no_listed_salary
known_email = people_in_dataset - no_known_email

print '\nQuantified salaries:', quantified_salaries

print '\nKnown emails:', known_email

total_payments_not_known = people_in_dataset - len(featureFormat(enron_data, ['total_payments']))
print '\nUnknown total payments:', total_payments_not_known

poi_with_no_total_payments = 0
for i in enron_data:
    if enron_data[i]['poi'] == True and enron_data[i]['total_payments'] == 'NaN':
        poi_with_no_total_payments += 1

print '\nPOIs with unknown total payments:', poi_with_no_total_payments