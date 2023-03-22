from matplotlib import pyplot
from kmeans import plot_kmeans
from threeDimensionalPlot import trhee_dimensional_plot
from plots import plots
import pandas

if __name__ == '__main__':

    data = pandas.read_csv('data/Dataset.csv', usecols=['price', 'distance_travelled(kms)', 'car_age', 'brand'])

    plots(data)

    trhee_dimensional_plot(data)

    data1 = pandas.read_csv('data/Dataset.csv', usecols=['price', 'distance_travelled(kms)'])

    print(data1.head())

    #  fill_interpolated_areas(k, clusters, values, color_map)
    pyplot.scatter(list(data1.iloc[:, 1]), list(data1.iloc[:, 0]), s=5, marker='o')
    pyplot.title("Price vs distance travelled")
    pyplot.xlabel('Distance travelled(kms)')
    pyplot.ylabel('Price')
    pyplot.semilogx()
    pyplot.show()

    # plot data as clasterized by kmeans

    number_of_clusters = 3
    plot_kmeans(data1, number_of_clusters)

    data2 = pandas.read_csv('data/Dataset.csv', usecols=['price','car_age'])
    print(data2.head())

    #  fill_interpolated_areas(k, clusters, values, color_map)
    pyplot.scatter(list(data2.iloc[:, 1]), list(data2.iloc[:, 0]), s=5, marker='o')
    pyplot.title("Price vs car age")
    pyplot.xlabel('Car Age')
    pyplot.ylabel('Price')
    pyplot.show()


    plot_kmeans(data2, 3)


