#Tim Tran
#1001638285

import sys, pandas as pd, numpy as np
from sklearn import preprocessing, model_selection, neighbors, svm
from collections import Counter
import matplotlib.pyplot as plt
from matplotlib import style
from itertools import product
style.use('ggplot')

class Support_Vector_Machine:
    def __init__(self, visualization=True):
        self.visualization = visualization
        self.colors = {1:'r',-1:'b'}
        if self.visualization:
            self.fig = plt.figure()
            self.ax = self.fig.add_subplot(1,1,1)
    
    def fit(self, data):
        print("This will take a while. Thus, I have printed the values of w so that you know the program is still running. Beware.")
        self.data = data
        opt_dict = {}
        le = preprocessing.LabelEncoder()
        
        if sys.argv[2] == "sonar.txt":
            transforms = np.array(list(product([-1,1], repeat = 60)))
        else:
            transforms = np.array(list(product([-1,1], repeat = 4)))
        
        all_data = []
        
        X = np.array(self.data.iloc[: , :-1])
        Y = self.data.iloc[:, -1]
        le.fit(Y)
        full = np.array(self.data)
        
        for yi in X:
            for featureset in yi:
                all_data.append(featureset)
        
        self.max_feature_value = max(all_data)
        self.min_feature_value = min(all_data)
        
        step_size = [self.max_feature_value*0.1]
        
        b_multiple_range = 5
        b_multiple = 5
        
        latest_optimum = self.max_feature_value*10
        
        for step in step_size:
            w = np.array([latest_optimum, latest_optimum, latest_optimum, latest_optimum])
            
            optimized = False
            
            while not optimized:
                for b in np.arange(-1*(self.max_feature_value*b_multiple_range), self.max_feature_value*b_multiple_range, step*b_multiple):
                    for transformation in transforms:
                        w_t = w*transformation
                        
                        for i in range(len(full)):
                            found_option = True
                            yi = Y[i]
                            if not yi*(np.dot(w_t, X[i])+b) >= 1:
                                found_option = False
                                continue
                    
                            if found_option:
                                opt_dict[np.linalg.norm(w_t)] = [w_t, b]
                        
                if w[0] < 0:
                    optimized = True
                    print('Optimized a step')
                else:
                    w = w-step
                    print(w)
            
        norm = sorted([n for n in opt_dict])
        
        opt_choice = opt_dict[norm[0]]
        
        self.w = opt_choice[0]
        self.b = opt_choice[1]
        
        latest_optimum = opt_choice[0][0]+step
    
    def predict(self,features):
        classification = np.sign(np.dot(np.array(features), self.w)+self.b)
        return classification

class MLChoice:
    def __init__(self, ML, DataSet):
        self.ML = ML
        self.DataSet = DataSet
        
    def SVM_function(self):
        X = np.array(self.DataSet.iloc[: , :-1])
        Y = np.array(self.DataSet.iloc[:, -1])
        
        #Scratch part
        Scratch_SVM = Support_Vector_Machine()
        if(sys.argv[2] == "sonar.txt"):
            print("Unfortunately I did not reduce so sonar will crash with the amount of data points. Beware")
        else:
            Scratch_SVM.fit(self.DataSet)
        if sys.argv[2] == "sonar.txt":
            prediction = "Doesn't exist because I didn't reduce"
        else:
            prediction = Scratch_SVM.predict([1.2572,4.8731,-5.2861,-5.8741])


        #SKlearn part
        X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size=0.2)

        clf = svm.SVC()

        clf.fit(X_train, Y_train)
        if sys.argv[2] == "sonar.txt":
            yes = [0.0200,0.0371,0.0428,0.0207,0.0954,0.0986,0.1539,0.1601,0.3109,0.2111,0.1609,0.1582,0.2238,0.0645,0.0660,0.2273,0.3100,0.2999,0.5078,0.4797,0.5783,0.5071,0.4328,0.5550,0.6711,0.6415,0.7104,0.8080,0.6791,0.3857,0.1307,0.2604,0.5121,0.7547,0.8537,0.8507,0.6692,0.6097,0.4943,0.2744,0.0510,0.2834,0.2825,0.4256,0.2641,0.1386,0.1051,0.1343,0.0383,0.0324,0.0232,0.0027,0.0065,0.0159,0.0072,0.0167,0.0180,0.0084,0.0090,0.0032]
        else:
            yes = [1.2572,4.8731,-5.2861,-5.8741]
        sk = clf.predict([yes])
        confidence = clf.score(X_test, Y_test)
        
        f = open('output.txt', 'w')

        f.write('Tim Tran\n1001638285\n\n')
        f.write('DataSet: %s\n' % (sys.argv[2]))
        f.write('Machine Learning Algorithm Chose: SVM\n')
        f.write('Scratch SVM Accuracy: Does not exist\n')
        f.write('ScikitLearn SVM Accuracy: %.3f%%\n' % (confidence*100))
        f.write('Prediction Point: ')
        f.write(str(yes))
        f.write('\nPredicted Class: ')
        f.write(str(prediction))
        f.write('\nSK Class: %s' % (str(sk)))
        f.close()
        
    def KNN_function(self):
        X = np.array(self.DataSet.iloc[: , :-1])
        Y = np.array(self.DataSet.iloc[:, -1])
        
        if sys.argv[2] == "sonar.txt":
            predict = [0.0262,0.0582,0.1099,0.1083,0.0974,0.2280,0.2431,0.3771,0.5598,0.6194,0.6333,0.7060,0.5544,0.5320,0.6479,0.6931,0.6759,0.7551,0.8929,0.8619,0.7974,0.6737,0.4293,0.3648,0.5331,0.2413,0.5070,0.8533,0.6036,0.8514,0.8512,0.5045,0.1862,0.2709,0.4232,0.3043,0.6116,0.6756,0.5375,0.4719,0.4647,0.2587,0.2129,0.2222,0.2111,0.0176,0.1348,0.0744,0.0130,0.0106,0.0033,0.0232,0.0166,0.0095,0.0180,0.0244,0.0316,0.0164,0.0095,0.0078]
        else:
            predict = [1.2572,4.8731,-5.2861,-5.8741]
        
        distances = []
        k=3
        
        #Scratch part
        for row in range(len(X)):
            euclid_distance = np.linalg.norm(np.array(X[row])-np.array(predict))
        
            distances.append([euclid_distance, Y[row]])
        
            
        votes = [i[1] for i in sorted(distances)[:k]]
        vote_result = Counter(votes).most_common(1)[0][0]
        scratch_confidence = Counter(votes).most_common(1)[0][1]/k

        #SKlearn part
        X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size=0.2)

        neigh = neighbors.KNeighborsClassifier(n_neighbors=k)
        
        neigh.fit(X_train, Y_train)
        if sys.argv[2] == "sonar.txt":
            sk = neigh.predict([[0.0262,0.0582,0.1099,0.1083,0.0974,0.2280,0.2431,0.3771,0.5598,0.6194,0.6333,0.7060,0.5544,0.5320,0.6479,0.6931,0.6759,0.7551,0.8929,0.8619,0.7974,0.6737,0.4293,0.3648,0.5331,0.2413,0.5070,0.8533,0.6036,0.8514,0.8512,0.5045,0.1862,0.2709,0.4232,0.3043,0.6116,0.6756,0.5375,0.4719,0.4647,0.2587,0.2129,0.2222,0.2111,0.0176,0.1348,0.0744,0.0130,0.0106,0.0033,0.0232,0.0166,0.0095,0.0180,0.0244,0.0316,0.0164,0.0095,0.0078]])
        else:
            sk = neigh.predict([[1.2572,4.8731,-5.2861,-5.8741]])
        
        confidence = neigh.score(X_test, Y_test)
        
        f = open('output.txt', 'w')

        f.write('Tim Tran\n1001638285\n\n')
        f.write('DataSet: %s\n' % (sys.argv[2]))
        f.write('Machine Learning Algorithm Chose: KNN\n')
        f.write('Scratch KNN Accuracy: %.3f%%\n' % (scratch_confidence*100))
        f.write('ScikitLearn KNN Accuracy: %.3f%%\n' % (confidence*100))
        f.write('Prediction Point: ')
        f.write(str(predict))
        f.write('\nPredicted Class: ')
        f.write(str(vote_result))
        f.write('\nSK Class: %s' % (str(sk)))
        f.close()



#Main Function
ML = sys.argv[1]
DataSet = pd.read_csv(sys.argv[2], header=None)

if(ML == "SVM"):
    Choice = MLChoice("SVM", DataSet)
    Choice.SVM_function()
    
else:
    Choice = MLChoice("KNN", DataSet)
    Choice.KNN_function()