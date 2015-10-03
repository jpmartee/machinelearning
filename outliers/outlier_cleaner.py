#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        clean away the 10% of points that have the largest
        residual errors (different between the prediction
        and the actual net worth)

        return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error)
    """
    
    cleaned_data = []

    ### explore training data thinking of each point as tuple (pred(ages_train), ages_train, net_worths_train)
    error = []
    for i in range(len(ages)):
        ### for each tuple compare pred(ages_train) and net_worths_train
        diff = predictions[i] - net_worths[i]
        error.append(abs(diff))
        tup = ages[i], net_worths[i], diff
        cleaned_data.append(tup)

    ### order the tuples by abs(pred(ages_train) - net_worths_train)
    ### collect the first 90% of the tuples
    cleaned_data.sort(key=lambda tup: tup[2])
    cleaned_data = cleaned_data[:int(0.9*(len(cleaned_data)))]

    return cleaned_data

