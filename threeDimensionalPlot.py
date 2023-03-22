import plotly.graph_objs as go
import plotly as py
from sklearn.cluster import KMeans
from matplotlib import pyplot
import numpy as np


def trhee_dimensional_plot(data):

        X3 = data[['price', 'distance_travelled(kms)', 'car_age']].iloc[:, :].values
        inertia = []
        for n in range(1, 11):
            algorithm = (KMeans(n_clusters=n, init='k-means++', n_init=10, max_iter=300,
                                tol=0.0001, random_state=111, algorithm='elkan'))
            algorithm.fit(X3)
            inertia.append(algorithm.inertia_)

        pyplot.figure(1, figsize=(15, 6))
        pyplot.plot(np.arange(1, 11), inertia, 'o')
        pyplot.plot(np.arange(1, 11), inertia, '-', alpha=0.5)
        pyplot.xlabel('Number of Clusters'), pyplot.ylabel('Inertia')
        pyplot.show()

        algorithm = (KMeans(n_clusters=3, init='k-means++', n_init=10, max_iter=300,
                            tol=0.0001, random_state=111, algorithm='elkan'))
        algorithm.fit(X3)
        labels3 = algorithm.labels_
        centroids3 = algorithm.cluster_centers_

        data['label3'] = labels3
        trace1 = go.Scatter3d(
            x=data['price'],
            y=data['distance_travelled(kms)'],
            z=data['car_age'],
            mode='markers',
            marker=dict(
                color=data['label3'],
                size=20,
                line=dict(
                    color=data['label3'],
                    width=12
                ),
                opacity=0.8
            )
        )
        data = [trace1]
        layout = go.Layout(
            title='Clusters',
            scene=dict(
                xaxis=dict(title='price'),
                yaxis=dict(title='distance_travelled(kms)'),
                zaxis=dict(title='car_age')
            )
        )
        fig = go.Figure(data=data, layout=layout)
        py.offline.plot(fig)