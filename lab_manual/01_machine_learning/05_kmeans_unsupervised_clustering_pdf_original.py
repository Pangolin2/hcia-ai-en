from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


X, y = make_blobs(n_samples=500, n_features=2, centers=4, random_state=1)

print("Dimension of X is {}".format(X.shape))
print("Dimension of y is {}".format(y.shape))

fig, ax1 = plt.subplots(1)
ax1.scatter(X[:, 0], X[:, 1],
            marker='o', # Set the shape of the point to circle.
            s=8 # Set the size of the point.
            )
plt.show()

color = ["red", "pink", "orange", "green"]
fig, ax1 = plt.subplots(1)

for i in range(4):
    ax1.scatter(X[y == i, 0], X[y == i, 1], # Draw the color based on the label.
                marker='o', # Set the shape of the point to circle.
                s=8, # Set the size of the point.
                c=color[i]
                )
plt.show()

n_clusters = 3
cluster1 = KMeans(n_clusters=n_clusters, random_state=3).fit(X)

y_pred1 = cluster1.labels_
print(y_pred1)

centroid1 = cluster1.cluster_centers_
print(centroid1)

color = ["red", "pink", "orange", "gray"]

fig, ax1 = plt.subplots(1)

for i in range(n_clusters):
    ax1.scatter(X[y_pred1 == i, 0], X[y_pred1 == i, 1],
                marker='o', # Set the shape of the point to circle.
                s=8, # Set the size of the point.
                c=color[i]
                )

ax1.scatter(centroid1[:, 0], centroid1[:, 1],
            marker="x",
            s=15,
            c="black")
plt.show()

n_clusters = 4
cluster2 = KMeans(n_clusters=n_clusters, random_state=0).fit(X)
y_pred2 = cluster2.labels_
centroid2 = cluster2.cluster_centers_
print("Centroid: {}".format(centroid2))

color = ["red", "pink", "orange", "green"]

fig, ax1 = plt.subplots(1)

for i in range(n_clusters):
    ax1.scatter(X[y_pred2 == i, 0], X[y_pred2 == i, 1],
                marker='o', # Set the shape of the point to circle.
                s=8, # Set the size of the point.
                c=color[i]
                )

ax1.scatter(centroid2[:, 0], centroid2[:, 1],
            marker="x",
            s=15,
            c="black")
plt.show()
