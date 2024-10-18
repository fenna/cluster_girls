# 1. Data voorbereiden
# Voordat je clustering uitvoert, moet je data verzamelen en voorbereiden. 
# Zorg ervoor dat de data numeriek en geschaald zijn, aangezien K-means gebruikmaakt van Euclidische afstand, waarbij de schaal van de variabelen invloed kan hebben.

# 2. Bepaal het aantal clusters 𝑘
# Dit kan worden gedaan op basis van domeinkennis of door een evaluatiemethode, zoals de "Elbow method" 

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt


def apply_standard_scaling(data):
    """Standardize the dataset (mean=0, variance=1)."""
    scaler = StandardScaler()
    return scaler.fit_transform(data)

def apply_kmeans(data, n_clusters=8):
    """Apply KMeans clustering and return labels and centroids."""
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    kmeans.fit(data)
    return kmeans.labels_, kmeans.cluster_centers_

def apply_pca(data, n_components=2):
    """Reduce the dimensionality of the dataset using PCA."""
    pca = PCA(n_components=n_components)
    return pca.fit_transform(data)

def plot_clusters(pca_data, labels, centroids):
    """Plot the PCA-reduced data with cluster assignments."""
    plt.figure(figsize=(8, 6))
    
    # Plot the data points with their cluster labels
    scatter = plt.scatter(pca_data[:, 0], pca_data[:, 1], c=labels, cmap='viridis', alpha=0.5)
    
    # Plot the cluster centroids
    plt.scatter(centroids[:, 0], centroids[:, 1], s=300, c='red', label='Centroids', marker='X')
    
    plt.title('PCA of Clusters')
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.legend()
    plt.colorbar(scatter)
    plt.show()

# Main pipeline

def main(data):
    # Step 1: Standardize the data (optional, but recommended)
    data = apply_standard_scaling(data)

    # Step 2: Apply KMeans clustering
    k = 8  # Number of clusters
    labels, centroids = apply_kmeans(data, n_clusters=k)

    # Step 3: Apply PCA for 2D visualization
    pca_data = apply_pca(data)

    # Step 4: Plot the clusters
    # Since centroids are in the original space, we need to apply PCA to centroids as well
    pca_centroids = apply_pca(centroids, n_components=2)
    plot_clusters(pca_data, labels, pca_centroids)


data = pd.read_csv('wijken.csv')
data = data.set_index('Codering_3')
main(data)

