import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from sklearn . linear_model import LogisticRegression
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix , ConfusionMatrixDisplay, classification_report




X, y = make_classification(n_samples=200, n_features=2, n_redundant=0, n_informative=2,
                            random_state=213, n_clusters_per_class=1, class_sep=1)

# train test split 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=5)


#a)
colors = ['red', 'blue']

plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train, cmap=plt.cm.colors.ListedColormap(colors))
plt.scatter(X_test[:, 0], X_test[:, 1], c=y_test, cmap=plt.cm.colors.ListedColormap(colors), marker='x')
plt.xlabel('x1')
plt.ylabel('x2')


#b)
LogRegression_model = LogisticRegression ()
LogRegression_model.fit( X_train , y_train )


#c)
theta0 = LogRegression_model.intercept_
theta1 = LogRegression_model.coef_[0,0]
theta2 = LogRegression_model.coef_[0,1]

x_min, x_max = np.min(X_train[:, 1]), np.max(X_train[:, 1])

x2 = np.linspace(x_min, x_max, 100)
x1 = -theta0/theta1 -theta2/theta1*x2

plt.plot(x1, x2)

plt.fill_between(x1, x2, x_min, alpha=0.2, color='blue')
plt.fill_between(x1, x2, x_max, alpha=0.2, color='red')

plt.show()


#d)
y_test_p = LogRegression_model.predict(X_test)

cm = confusion_matrix(y_test, y_test_p)
print("confusion_matrix : ", cm)
disp = ConfusionMatrixDisplay(confusion_matrix(y_test, y_test_p))
disp.plot ()
plt.show ()

print(classification_report(y_test, y_test_p)) 


#e)
colors = ['k' if y_test[i] != y_test_p[i] else 'g' for i in range(len(y_test))]
plt.scatter(X_test[:, 0], X_test[:, 1], c=colors)
plt.xlabel('x1')
plt.ylabel('x2')
plt.show()
