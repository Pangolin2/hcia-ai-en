import pandas as pd
import numpy as np
from sklearn import tree
import pydotplus


# Generate a decision tree.
def createTree(trainingData):
    data = trainingData.iloc[:, :-1] # Feature matrix
    labels = trainingData.iloc[:, -1] # Labels
    trainedTree = tree.DecisionTreeClassifier(criterion="entropy") # Decision tree classifier
    trainedTree.fit(data, labels) # Train the model.
    return trainedTree


def showtree2pdf(trainedTree, finename):
    dot_data = tree.export_graphviz(trainedTree, out_file=None) # Export the tree in Graphviz format.
    graph = pydotplus.graph_from_dot_data(dot_data)
    graph.write_pdf(finename) # Save the tree diagram to the local machine in PDF format.


def data2vectoc(data):
    names = data.columns[:-1]
    for i in names:
        col = pd.Categorical(data[i])
        data[i] = col.codes
    return data


data = pd.read_table("./ML/tennis.txt", header=None, sep='\t') # Read training data.
trainingvec = data2vectoc(data) # Vectorize data.
decisionTree = createTree(trainingvec) # Create a decision tree.
showtree2pdf(decisionTree, "tennis.pdf") # Plot the decision tree.

testVec = [0, 0, 1, 1] # Weather is sunny, temperature is low, humidity is high, and wind is strong.
print(decisionTree.predict(np.array(testVec).reshape(1, -1))) # Predict.
