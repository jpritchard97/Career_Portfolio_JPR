# Decision Tree Analysis: Learning Tool from HyperionDev Bootcamp

## Introduction
This document presents an analysis of a decision tree model, created as part of a lecture within the HyperionDev bootcamp. It serves as a learning tool to understand the process of importing packages, loading datasets, creating target identification, initiating decision trees, performing pruning, and visualizing results.


```python
# data processing and cleaning
import numpy as np

# Machine Learning
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Decision tree classifier
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree

# Visualisation
import matplotlib.pyplot as plt
from sklearn.tree import export_graphviz
from IPython.display import Image
from subprocess import call
```


```python
# Load the iris dataset from seaborn
iris = load_iris()

# Locate the target variables
x = iris.data[:, ]
y = iris.target

r = 4
X_train, X_test, y_train, y_test = train_test_split(x, y,test_size=0.25, random_state=r)
```


```python
# Instantiate a DecisionTreeClassifier without any pruning
unpruned = DecisionTreeClassifier(max_depth=None, random_state=r)

# Train the unpruned decision tree model on the training data
unpruned.fit(X_train, y_train)

# Evaluate the performance of the unpruned model on the test set
print('Performance without pruning:', unpruned.score(X_test, y_test))

# Check the maximum depth of the unpruned decision tree
print('Maximum depth of the unpruned tree:', unpruned.tree_.max_depth)

```

    Performance without pruning: 0.9736842105263158
    Maximum depth of the unpruned tree: 4


## Pruning the Decision Tree

- In this section of code, we prune the decision tree by evaluating its performance at different maximum depths. 

- Pruning helps prevent overfitting and improves the generalization ability of the model.


```python
# Define the range of maximum depths to prune the decision tree
pruned_depths = range(1, unpruned.tree_.max_depth + 1)

# Initialize an empty list to store the accuracy scores for pruned trees
pruned_scores = []

# Iterate over each depth value for pruning
for d in pruned_depths:
    # Instantiate a DecisionTreeClassifier with the specified maximum depth for pruning
    clf = DecisionTreeClassifier(max_depth=d, random_state=r)
    
    # Train the pruned decision tree model on the training data
    clf.fit(X_train, y_train)
    
    # Evaluate the performance of the pruned model on the test set
    score = clf.score(X_test, y_test)
    
    # Append the accuracy score to the list of pruned_scores
    pruned_scores.append(score)

# Plot the accuracy scores against the maximum depth values used for pruning
fig, ax = plt.subplots()
ax.plot(pruned_depths, pruned_scores)
plt.xlabel('Max_depth values')
plt.ylabel('Accuracy')
ax.xaxis.set_ticks(pruned_depths)
plt.show()

```


    
![png](Decision_Trees_files/Decision_Trees_5_0.png)
    


## What does this tell us?

- The best depth for the decision tree model was found at layer 2, which corresponds to the lowest index of the highest score achieved during the evaluation process.

## What Now?

(1) Print accuracy scores obtained for different maximum depths after pruning.

(2) Determine the best depth by finding the index of the maximum accuracy score in pruned_scores.

(3) Print the best performance reached along with its corresponding depth.

(4) Instantiate the DecisionTreeClassifier with the best depth found.

(5) Train the pruned decision tree model on the entire dataset x and y.


```python
# Print the accuracy scores obtained for different maximum depths after pruning
print(pruned_scores)

# Determine the best depth based on the maximum accuracy score achieved
best_depth = pruned_depths[np.argmax(pruned_scores)]

# Print the best performance reached along with its corresponding depth
print('Best performance reached at depth of:', best_depth)

# Instantiate a DecisionTreeClassifier with the best depth found
pruned = DecisionTreeClassifier(max_depth=best_depth)

# Train the pruned decision tree model on the entire dataset
pruned.fit(x, y)

```

    [0.6842105263157895, 0.9736842105263158, 0.9736842105263158, 0.9736842105263158]
    Best performance reached at depth of: 2