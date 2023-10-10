#Tim Tran
#1001638285

from scipy.stats import norm
from sklearn.naive_bayes import GaussianNB
from numpy import mean
from numpy import std
import sys, csv, numpy as np

def fit_distribution(data):
    mu = mean(data)
    sigma = std(data)
    dist = norm(mu, sigma)
    return dist

def probability(X, prior, dist1, dist2, dist3):
    return prior * dist1.pdf(X[0]) * dist2.pdf(X[1]) * dist3.pdf(X[2])

def naive_bayes():

    results = []
    with open(sys.argv[1]) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            results.append(row)


    X1 = []
    Y1 = []
    for row in range(len(results)):
        new = []
        for i in range(4):
            new.append(float(results[row][i]))
        if results[row][4] == "Iris-setosa":
            Y1.append(0)
        elif results[row][4] == "Iris-versicolor":
            Y1.append(1)
        else:
            Y1.append(2)
        X1.append(new)

    X = np.array(X1)
    Y = np.array(Y1)

    Xy_Setosa = X[Y == 0]
    Xy_Versicolor = X[Y == 1]
    Xy_Virginica = X[Y == 2]


    priory0 = len(Xy_Setosa) / len(X)
    priory1 = len(Xy_Versicolor) / len(X)
    priory2 = len(Xy_Virginica) / len(X)

    distX1y_Setosa = fit_distribution(Xy_Setosa[:, 0])
    distX2y_Setosa = fit_distribution(Xy_Setosa[:, 1])
    distX3y_Setosa = fit_distribution(Xy_Setosa[:, 2])

    distX1y_Versicolor = fit_distribution(Xy_Versicolor[:, 0])
    distX2y_Versicolor = fit_distribution(Xy_Versicolor[:, 1])
    distX3y_Versicolor = fit_distribution(Xy_Versicolor[:, 2])

    distX1y_Virginica = fit_distribution(Xy_Virginica[:, 0])
    distX2y_Virginica = fit_distribution(Xy_Virginica[:, 1])
    distX3y_Virginica = fit_distribution(Xy_Virginica[:, 2])

    Xsample, ysample = X[0], Y[0]
    py0 = probability(Xsample, priory0, distX1y_Setosa, distX2y_Setosa, distX3y_Setosa)
    py1 = probability(Xsample, priory1, distX1y_Versicolor, distX2y_Versicolor, distX3y_Versicolor)
    py2 = probability(Xsample, priory2, distX1y_Virginica, distX2y_Virginica, distX3y_Virginica)

    print('P(y=0 | %s) = %.3f' % (Xsample, py0*100))
    print('P(y=1 | %s) = %.3f' % (Xsample, py1*100))
    print('P(y=2 | %s) = %.3f' % (Xsample, py2*100))
    print('Truth: y = %d' % ysample)


#Gaussian_NB comparison

    clf = GaussianNB()
    clf.partial_fit(X, Y, np.unique(Y))

    f = open('output.txt', 'w')

    f.write('Tim Tran\n1001638285\n\n')
    

    correct = 0
    total = 0

    for i in range(len(X)):
        final = 0
        py = probability(X[i], priory0, distX1y_Setosa, distX2y_Setosa, distX3y_Setosa)
        py_1 = probability(X[i], priory1, distX1y_Versicolor, distX2y_Versicolor, distX3y_Versicolor)
        py_2 = probability(X[i], priory2, distX1y_Virginica, distX2y_Virginica, distX3y_Virginica)
        if (py > py_1) and (py > py_2):
           final = 0
        elif (py_1 > py) and (py_1 > py_2):
           final = 1
        else:
           final = 2
        if final == Y[i]:
            correct = correct+1
            total = total+1
        else:
            total = total+1
   
    f.write('Implemented Naive Bayes Accuracy: %.3f%%' % ((correct/total)*100))

    f.write('\nScikitLearn Gaussian Naive Bayes Accuracy: %.3f%%' % (clf.score(X, Y)*100))
    
naive_bayes()