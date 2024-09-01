import numpy as np

    
def initialize_centroids(data, k):
    indices = np.random.choice(data.shape[0], k, replace=False)
    return data[indices]

def assign_clusters(data, centroids):
    clusters = []
    for point in data:
        distances = np.sqrt(np.sum((centroids - point)**2, axis=1))
        closest_centroid = np.argmin(distances)
        clusters.append(closest_centroid)
    return np.array(clusters)

def update_centroids(data, clusters, k):
    new_centroids = np.zeros((k, data.shape[1]))
    for i in range(k):
        cluster_points = data[clusters == i]
        if len(cluster_points) > 0:
            new_centroids[i] = np.mean(cluster_points, axis=0)
        else:
            # If a cluster is empty, randomly reinitialize it
            new_centroids[i] = data[np.random.choice(data.shape[0])]
    return new_centroids

def has_converged(old_centroids, new_centroids, tolerance):
    return np.all(np.sqrt(np.sum((old_centroids - new_centroids)**2, axis=1)) < tolerance)

def kmeans(data, k, max_iterations=100, tolerance=1e-4):
    centroids = initialize_centroids(data, k)
    
    for _ in range(max_iterations):
        clusters = assign_clusters(data, centroids)
        old_centroids = centroids.copy()
        centroids = update_centroids(data, clusters, k)
        
        if has_converged(old_centroids, centroids, tolerance):
            break
    
    return centroids, clusters

# Example usage
if __name__ == "__main__":
    np.random.seed(42)
    data = np.random.randn(100, 2) * 2
    data = np.vstack((data, np.random.randn(50, 2) + np.array([5, 5])))
    data = np.vstack((data, np.random.randn(50, 2) + np.array([-5, 5])))
    
    k = 3  # Number of clusters
    centroids, clusters = kmeans(data, k)
    
    print("\nFinal centroids:")
    print(centroids)
    print("\nNumber of points in each cluster:", np.bincount(clusters))
   