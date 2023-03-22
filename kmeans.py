from pandas import DataFrame
from numpy import count_nonzero
from random import sample
from math import sqrt
import numpy
from matplotlib import pyplot
from scipy.spatial import ConvexHull
from scipy import interpolate


def kmeans(values, k):
    clusters = []
    for _ in range(len(values)):
        clusters.append(0)

    centers_of_clusters = sample(list(values), k)

    while True:
        for j, value in enumerate(values):
            min_dist = float('inf')
            for cluster_number, centroid in enumerate(centers_of_clusters):
                dist = sqrt((centroid[0] - value[0]) ** 2 + (centroid[1] - value[1]) ** 2)
                if dist < min_dist:
                    min_dist = dist
                    clusters[j] = cluster_number
        new_centroids = DataFrame(values).groupby(by=clusters).mean().values
        if k == 2 or not count_nonzero(centers_of_clusters - new_centroids):
            break
        else:
            centers_of_clusters = new_centroids
    return centers_of_clusters, clusters


def plot_kmeans(data, k):
    values = data.values
    centroids, clusters = kmeans(values, k)
    color_map = pyplot.cm.get_cmap("hsv", k + 1)

    for value_number, value in enumerate(values):
        pyplot.scatter(value[1], value[0], s=5, marker='o', color=color_map(clusters[value_number]))

    # points for centroids
    for k, centroid in enumerate(centroids):
        pyplot.scatter(centroid[1], centroid[0], s=25, marker='x', color='black')

    pyplot.title("Cars grouped by kmeans")
    pyplot.ylabel('Price')
    pyplot.xlabel('Car Age')
    pyplot.semilogx()
    pyplot.show()
