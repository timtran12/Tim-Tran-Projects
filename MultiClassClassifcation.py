#Tim Tran
#1001638285

import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn import svm
from sklearn.model_selection import train_test_split
import fpdf

Dataset = pd.read_csv("glass.txt", header=None)

X = np.array(Dataset.iloc[: , :-1])
Y = np.array(Dataset.iloc[:, -1])

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=.3)

model = svm.SVC(kernel='linear')
model.fit(x_train, y_train)
train_predictions = model.predict(x_train)
predictions = model.predict(x_test)
train_acc = accuracy_score(train_predictions, y_train) 
accuracy = accuracy_score(predictions, y_test)

pdf = fpdf.FPDF(format='letter')
pdf.add_page()
pdf.set_font("Arial", size=12)

pdf.write(5,"Tim Tran")
pdf.ln()
pdf.write(5,"1001638285")
pdf.ln()
pdf.write(5,"Machine Learning Algorithm: SVM")
pdf.ln()
pdf.write(5,"Library: Sklearn")
pdf.ln()
pdf.write(5,"Training accuracy: %.2f%%" % (train_acc*100))
pdf.ln()
pdf.write(5,"Testing accuracy: %.2f%%" % (accuracy*100))

pdf.output("output.pdf")