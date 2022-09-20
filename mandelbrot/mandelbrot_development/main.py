"""TODO"""

import numpy
import matplotlib.pyplot as plt

class Mandelbrot:
    """TODO"""

    def __init__(self):
        """TODO"""
        self.x_value_start = 0
        self.x_value_end = 0
        self.x_number_of_values = 0
        self.x_values = None
        self.y_value_start = 0
        self.y_value_end = 0
        self.y_number_of_values = 0
        self.y_values = None
        self.atlas = None

    def mandel(self, c, maxiter):
        """TODO"""
        z = complex(0, 0)

        for iteration in range(maxiter):
            z = (z*z) + c

            if abs(z) > 4:
                break

        return iteration


    def x_numeric_sequence(self):
        """TODO"""
        self.x_values = numpy.linspace(self.x_value_start, self.x_value_end, self.x_number_of_values)

    def y_numeric_sequence(self):
        """TODO"""
        self.y_values = numpy.linspace(self.y_value_start, self.y_value_end, self.y_number_of_values)


    def atlas_create(self):
        """TODO"""
        xlen = len(self.x_values)
        ylen = len(self.y_values)

        self.atlas = numpy.zeros((xlen, ylen))

        for ix in range(xlen):
            for iy in range(ylen):
                cx = self.x_values[ix]
                cy = self.y_values[iy]
                c = complex(cx, cy)
                self.atlas[ix, iy] = self.mandel(c, 120)

    def draw(self):
        """TODO"""

        plt.figure(figsize=(18, 18))
        plt.imshow(self.atlas.T,
               interpolation="nearest")
        plt.show()

    def __str__(self):
        """TODO"""
        return f'{self.x_values}'

    def __repr__(self):
        """TODO"""
        return f'{self.x_number_of_values}'

def main():
    """TODO"""
    mb = Mandelbrot()
    mb.x_value_start = -0.22
    mb.x_value_end = -0.21
    mb.x_number_of_values = 1000
    mb.x_numeric_sequence()

    mb.y_value_start = -0.70
    mb.y_value_end = -0.69
    mb.y_number_of_values = 1000
    mb.y_numeric_sequence()
    
    mb.atlas_create()
    mb.draw()

if __name__ == "__main__":
    main()
