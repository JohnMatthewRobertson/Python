""" add better comments """
import csv
import numpy
import matplotlib.pyplot


def load_csv(file_name):
    """add better comments """
    with open(file_name, newline='') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            print(row)
            image_array = numpy.asfarray(row[1:]).reshape((28,28))
            matplotlib.pyplot.imshow(image_array, cmap='Greys', interpolation='None')
            matplotlib.pyplot.show()

