import numpy as np


class Variable:
    def __init__(self, data):
        self.data = data
        self.grad = None
        self.creator = None

    def self.creator(self, func):
        self.creator = func

    def backward(self):
        funcs = [self.creator]
        