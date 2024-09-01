
# K-Means Clustering

This repository contains a simple implementation of the K-Means clustering algorithm in Python using NumPy. K-Means is an unsupervised learning algorithm used to partition a dataset into `k` distinct, non-overlapping clusters.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Functions](#functions)
- [Example](#example)
- [Contributing](#contributing)

## Features

- Random initialization of centroids.
- Assignment of points to the nearest centroid.
- Update of centroids based on the mean of assigned points.
- Convergence check based on centroid movement within a specified tolerance.
- Handling of empty clusters by reinitializing them.

## Installation

To use this code, ensure that you have Python installed along with the NumPy library. You can install NumPy using pip if it is not already installed:

```bash
pip install numpy
```

## Usage

You can use this K-Means implementation by importing the functions into your project or by running the provided example in the code.

### Basic Flow

1. **Initialize Centroids:** Randomly choose `k` points from the dataset as the initial centroids.
2. **Assign Clusters:** Assign each data point to the nearest centroid.
3. **Update Centroids:** Calculate the new centroids as the mean of the points assigned to each cluster.
4. **Check Convergence:** Check if the centroids have moved less than a defined tolerance. If not, repeat the process.

## Functions

### `initialize_centroids(data, k)`
- Initializes `k` centroids by randomly selecting points from the dataset.

### `assign_clusters(data, centroids)`
- Assigns each data point to the closest centroid.

### `update_centroids(data, clusters, k)`
- Updates the centroids by calculating the mean of all points in each cluster.

### `has_converged(old_centroids, new_centroids, tolerance)`
- Checks if the centroids have moved less than the specified tolerance.

### `kmeans(data, k, max_iterations=100, tolerance=1e-4)`
- Runs the K-Means clustering algorithm on the provided dataset.

## Example

An example of how to use this K-Means implementation is included in the code. To run the example:

```bash
python kmeans.py
```

This will generate a synthetic dataset, apply the K-Means algorithm to it, and print the final centroids along with the number of points in each cluster.

Example Output:

```bash
Final centroids:
[[ 4.83551076  5.0211162 ]
 [-4.77824038  4.80491724]
 [-0.18743006  0.21172187]]

Number of points in each cluster: [50 50 100]
```

## Contributing

If you want to contribute to this project, feel free to open an issue or submit a pull request.

