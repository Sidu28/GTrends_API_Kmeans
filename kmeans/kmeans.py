import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from time import time
from sklearn.cluster import KMeans
from sklearn import metrics
from sklearn.decomposition import PCA
from sklearn.datasets import load_digits
from sklearn.preprocessing import scale



def k_means_performance(estimator, name, data, labels):
    t0 = time()
    #cluster_indices = estimator.fit (data)
    estimator.fit (data)
    print('%-9s\t%.2fs\t%i\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f'
    % (name, (time() - t0), estimator.inertia_,
                   metrics.homogeneity_score(labels, estimator.labels_),
                   metrics.completeness_score(labels, estimator.labels_),
                   metrics.v_measure_score(labels, estimator.labels_),
                   metrics.adjusted_rand_score(labels, estimator.labels_),
                   metrics.adjusted_mutual_info_score(labels,  estimator.labels_)))
    #return cluster_indices
    
def PCA_2(data, clusters):
    reduced_data = PCA(n_components=2).fit_transform(data)
    kmeans = KMeans(init='k-means++', n_clusters=clusters, n_init=10)
    kmeans.fit(reduced_data)
    
    h = .02     # point in the mesh [x_min, x_max]x[y_min, y_max].

    # Plot the decision boundary. For that, we will assign a color to each
    x_min, x_max = reduced_data[:, 0].min() - 1, reduced_data[:, 0].max() + 1
    y_min, y_max = reduced_data[:, 1].min() - 1, reduced_data[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

    # Obtain labels for each point in mesh. Use last trained model.
    Z = kmeans.predict(np.c_[xx.ravel(), yy.ravel()])

    # Put the result into a color plot
    Z = Z.reshape(xx.shape)
    plt.figure(1)
    plt.clf()
    plt.imshow(Z, interpolation='nearest',
               extent=(xx.min(), xx.max(), yy.min(), yy.max()),
               cmap=plt.cm.Paired,
               aspect='auto', origin='lower')

    plt.plot(reduced_data[:, 0], reduced_data[:, 1], 'k.', markersize=2)
    # Plot the centroids as a white X
    centroids = kmeans.cluster_centers_
    plt.scatter(centroids[:, 0], centroids[:, 1],
                marker='x', s=169, linewidths=3,
                color='w', zorder=10)
    plt.title('K-means clustering on the digits dataset (PCA-reduced data)\n'
              'Centroids are marked with white cross')
    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)
    plt.xticks(())
    plt.yticks(())
    plt.show()


    

    
def k_means(filename):
    df = pd.read_csv(filename, header=0)
    n = len(df.columns)

    labels = df.iloc[:,-1]
    labels = (labels.to_numpy()).transpose()  #gets all the labels so we can check against our clustering
    labels=np.array(labels).flatten()  #converting labels into an array for processing metrics in k_means_performance
    clusters = len(np.unique(labels))    #gets the number of clusters based on the number of unique labels there are

    
    data = df[df.columns[:n-1]].to_numpy()  #extracts everything except the last column (which is just labels) as the data
    n_samples, n_features = data.shape

    #KMeans:
    estimator = KMeans(init='k-means++', n_clusters=clusters, n_init=10)
    cluster_indices = estimator.fit_predict(data)
    
    print(82 * '_')
    print('init\t\ttime\tinertia\thomo\tcompl\tv-meas\tARI\tAMI')
    print(82 * '_')
    k_means_performance(KMeans(init='k-means++', n_clusters=clusters, n_init=10), name="k-means++", data=data, labels = labels)  #gives us performance

    k_means_performance(KMeans(init='random', n_clusters=clusters, n_init=10),name="random", data=data, labels = labels)   #gives us performance
    
    pca = PCA(n_components=n_features).fit(data)
    k_means_performance(KMeans(init=pca.components_, n_clusters=clusters, n_init=9),
                  name="PCA-based",
                  data=data, labels = labels)
    print(82 * '_')

              
              
    #Visualize Data:
    PCA_2(data, clusters)
              
              
              
              
    #pca = PCA(n_components=clusters).fit(data)
    #k_means_performance(KMeans(init=pca.components_, n_clusters=clusters, n_init=1),
      #            name="PCA-based",
       #           data=data)
    

def main():
    filename = sys.argv[1]
    k_means(filename)
    
# This if-condition is True if this file was executed directly.
# It's False if this file was executed indirectly, e.g. as part
# of an import statement.
if __name__ == "__main__":
    main()



