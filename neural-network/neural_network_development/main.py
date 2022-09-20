""" creates and runs the neural network """

from neural_network import NeuralNetwork
from data_handler import load_csv

if __name__ == "__main__":

    load_csv('../mnist_data/mnist_test_10.csv')

    INPUT_NODES = 3
    HIDDEN_NODES = 3
    OUTPUT_NODES = 3
    LEARNING_RATE = 0.3
    TEST_QUERY = [1.0, 0.5, -1.5]

    neural_network = NeuralNetwork(
        INPUT_NODES, HIDDEN_NODES, OUTPUT_NODES, LEARNING_RATE)

    print(neural_network.query(TEST_QUERY))
