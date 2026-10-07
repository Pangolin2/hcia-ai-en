import pandas as pd
import matplotlib.pyplot as plt
from sklearn import tree


# Train a decision tree classifier.
def createTree(trainingData):
    data = trainingData.iloc[:, :-1]   # Feature matrix
    labels = trainingData.iloc[:, -1]  # Target labels

    trainedTree = tree.DecisionTreeClassifier(
        criterion="entropy",
        random_state=42
    )
    trainedTree.fit(data, labels)
    return trainedTree


# Display the decision tree directly as an image.
def showtree(trainedTree, feature_names):
    fig, ax = plt.subplots(figsize=(16, 10), dpi=120)

    tree.plot_tree(
        trainedTree,
        feature_names=[str(name) for name in feature_names],
        class_names=[str(label) for label in trainedTree.classes_],
        filled=True,       # Color nodes based on their classes.
        rounded=True,      # Use rounded node boxes.
        fontsize=10,       # Set the font size.
        precision=2,       # Set the number of decimal places.
        ax=ax
    )

    ax.set_title("Tennis Decision Tree", fontsize=16)
    fig.tight_layout()

    # Uncomment the following line to also save the image as a PNG file.
    # fig.savefig("tennis_tree.png", dpi=300, bbox_inches="tight")

    plt.show()


# Convert categorical features into numerical codes.
def data2vectoc(data):
    data = data.copy()

    for name in data.columns[:-1]:
        col = pd.Categorical(data[name])
        data[name] = col.codes

        # Print the encoding mapping to help prepare test data correctly.
        print(f"Feature {name} encoding: {dict(enumerate(col.categories))}")

    return data


# Load data: the last column contains labels; all other columns are features.
data = pd.read_table("./tennis.txt", header=None, sep="\t")

# Encode features and train the model.
trainingvec = data2vectoc(data)
decisionTree = createTree(trainingvec)

# Predict using numerical codes from the printed encoding mappings.
testVec = [0, 0, 1, 1]
testData = pd.DataFrame(
    [testVec],
    columns=trainingvec.columns[:-1]
)
print("Prediction:", decisionTree.predict(testData))

# Display the decision tree.
showtree(decisionTree, trainingvec.columns[:-1])
