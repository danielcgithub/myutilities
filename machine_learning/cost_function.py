#!/usr/bin/python
import numpy as np
from sklearn.datasets import load_boston
import matplotlib.pyplot as plt


def main():
    dataset = load_boston()
    X = dataset.data
    y = dataset.target[:, np.newaxis]
    print("Total samples in our dataset is: {}".format(X.shape[0]))
    print(X)
    print("----------------------------------------------------------")
    print(y)


def compute_cost(X, y, params):
    n_samples = len(y)
    h = X @ params
    return (1/(2*n_samples))*np.sum((h-y)**2)


if __name__ == "__main__":
    main()
