import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from collections import Counter
import sys


# The RandomForest algorithm should not need standardization

# Training the model

if len(sys.argv) != 2:
    print("There must be TWO arguments: the number of trees to use.")
    sys.exit()

trainingData = pd.read_csv("./labeled_data.csv")

labels = trainingData['IsFake']
trainingData.drop(['Unnamed: 0', 'ID', 'IsFake'], axis=1, inplace=True)

for i in range(trainingData.shape[0]):
    if trainingData.at[i, 'Following/follower ratio'] == float("inf"):
        trainingData.at[i, 'Following/follower ratio'] = 3.402823466e+38  # Max. number for a float32
    if trainingData.at[i, 'Following/post ratio'] == float("inf"):
        trainingData.at[i, 'Following/post ratio'] = 3.402823466e+38
    if trainingData.at[i, 'Follower/post ratio'] == float("inf"):
        trainingData.at[i, 'Follower/post ratio'] = 3.402823466e+38

y = labels.to_numpy()
X = trainingData.values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)


algo = RandomForestClassifier(n_estimators=int(sys.argv[1]))
algo.fit(X_train, y_train)
y_pred = algo.predict(X_test)

print('\nTraining data')
print("Accuracy score: ", accuracy_score(y_test, y_pred), sep="")
print("Confusion matrix:\n", confusion_matrix(y_test, y_pred), sep="")
print("[[TN, FP\n FN, TP]]\n")

# Applying the model

realData = pd.read_csv("./data_ready_for_analysis.csv")
realData.drop(['Unnamed: 0', 'ID'], axis=1, inplace=True)

for i in range(realData.shape[0]):
    if realData.at[i, 'Following/follower ratio'] == float("inf"):
        realData.at[i, 'Following/follower ratio'] = 3.402823466e+38  # Max. number for a float32
    if realData.at[i, 'Following/post ratio'] == float("inf"):
        realData.at[i, 'Following/post ratio'] = 3.402823466e+38
    if realData.at[i, 'Follower/post ratio'] == float("inf"):
        realData.at[i, 'Follower/post ratio'] = 3.402823466e+38

X_real = realData.values

y_real = algo.predict(X_real)

nbOfFakeAccounts = Counter(y_real)[True]
totalNbOfAccounts = y_real.shape[0]

print("Propotrion of fake accounts in the dataset: " + str(nbOfFakeAccounts/totalNbOfAccounts) + "\n")
