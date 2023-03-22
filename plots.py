
import seaborn as sns
from matplotlib import pyplot


def plots(data):
    print(data.describe())

    pyplot.figure(1, figsize=(15, 6))
    n = 0
    for x in ['price', 'distance_travelled(kms)', 'car_age']:
        n += 1
        pyplot.subplot(1, 3, n)
        pyplot.subplots_adjust(hspace=0.5, wspace=0.5)
        sns.distplot(data[x], bins=20)
        pyplot.title('Distplot of {}'.format(x))
    pyplot.show()

    pyplot.figure(1, figsize=(15, 7))
    pyplot.figure(1, figsize=(15, 5))
    sns.countplot(y='brand', data=data)
    pyplot.show()

    pyplot.figure(1, figsize=(15, 7))
    n = 0
    for x in ['price', 'distance_travelled(kms)', 'car_age']:
        for y in ['price', 'distance_travelled(kms)', 'car_age']:
            if x != y:
                n += 1
                pyplot.subplot(3, 3, n)
                pyplot.subplots_adjust(hspace=0.5, wspace=0.5)
                sns.regplot(x=x, y=y, data=data)
                pyplot.ylabel(y.split()[0] + ' ' + y.split()[1] if len(y.split()) > 1 else y)
    pyplot.show()

    pyplot.figure(1, figsize=(15, 6))
    for brand in ['Mercedes-Benz', 'Nissan', 'Skoda']:
        pyplot.scatter(x='price', y='distance_travelled(kms)',
                       data=data[data['brand'] == brand], s=200, alpha=0.5, label=brand)
    pyplot.xlabel('price'), pyplot.ylabel('distance_travelled(kms)')
    pyplot.title('Price vs distance travelled for few brands of cars')
    pyplot.legend()
    pyplot.show()

