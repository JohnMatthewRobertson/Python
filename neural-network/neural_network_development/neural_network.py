"""
 neural network class definition
"""

import numpy
import scipy.special


class NeuralNetwork:
    """ add better commments """

    def __init__(self, input_nodes, hidden_nodes, output_nodes, learning_rate):
        """ add better comments """
        self.input_nodes = input_nodes
        self.hidden_nodes = hidden_nodes
        self.output_nodes = output_nodes
        self.learning_rate = learning_rate

        self.weight_input_nodes_hidden_nodes = numpy.random.normal(
            0.0, pow(self.input_nodes, -0.5),
            (self.hidden_nodes, self.input_nodes))

        self.weight_hidden_nodes_output_nodes = numpy.random.normal(
            0.0, pow(self.hidden_nodes, -0.5),
            (self.output_nodes, self.hidden_nodes))

    def train(self, inputs_list, targets_list):
        """ add better comments """
        inputs = numpy.array(inputs_list, ndmin=2).T
        targets = numpy.array(targets_list, ndmin=2).T

        hidden_inputs = numpy.dot(self.weight_input_nodes_hidden_nodes, inputs)
        hidden_outputs = scipy.special.expit(hidden_inputs)
        final_inputs = numpy.dot(
            self.weight_hidden_nodes_output_nodes, hidden_outputs)
        final_outputs = scipy.special.expit(final_inputs)

        output_errors = targets - final_outputs
        hidden_errors = numpy.dot(
            self.weight_hidden_nodes_output_nodes.T, output_errors)

        self.weight_hidden_nodes_output_nodes += self.learning_rate * \
            numpy.dot((output_errors * final_outputs *
                      (1.0 - final_outputs)), numpy.transpose(hidden_outputs))

        self.weight_input_nodes_hidden_nodes += self.learning_rate * \
            numpy.dot((hidden_errors * hidden_outputs *
                      (1.0 - hidden_outputs)), numpy.transpose(inputs))

    def query(self, inputs_list):
        """ query the neural network
        convert inputs list to 2d array
        scipy.special.expit sigmoid function """

        # ndmin minimum number of dimensions of the array
        # .T transpose array
        inputs = numpy.array(inputs_list, ndmin=2).T

        hidden_inputs = numpy.dot(self.weight_input_nodes_hidden_nodes, inputs)
        hidden_outputs = scipy.special.expit(hidden_inputs)
        final_inputs = numpy.dot(
            self.weight_hidden_nodes_output_nodes, hidden_outputs)
        final_outputs = scipy.special.expit(final_inputs)

        return final_outputs
