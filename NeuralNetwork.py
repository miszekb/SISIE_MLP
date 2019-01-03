import time
import pprint
import numpy as np

class Neural_Network(object):

  loss = []
  learning_rate = 0.9

  def __init__(self):
    self.inputSize = 1
    self.outputSize = 1
    self.hiddenSize = 2
    self.W1 = np.random.randn(self.inputSize, self.hiddenSize)
    self.W2 = np.random.randn(self.hiddenSize, self.outputSize)

  def forward(self, X):
    self.z = np.dot(X, self.W1) 
    self.z2 = self.sigmoid(self.z)
    self.z3 = np.dot(self.z2, self.W2) 
    o = self.sigmoid(self.z3)
    return o 

  def sigmoid(self, s):
    return 1/(1+np.exp(-s))

  def sigmoidPrime(self, s):
    return s * (1 - s)

  def backward(self, X, y, o):
    self.o_error = y - o 
    self.o_delta = self.learning_rate * self.o_error*self.sigmoidPrime(o)
    self.z2_error = self.o_delta.dot(self.W2.T) 
    self.z2_delta = self.z2_error*self.sigmoidPrime(self.z2)
    self.W1 += X.T.dot(self.z2_delta) 
    self.W2 += self.z2.T.dot(self.o_delta) 

  def train (self, X, y):
    o = self.forward(X)
    self.backward(X, y, o)
