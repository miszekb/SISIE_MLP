import time
import pprint
import numpy as np

X = np.random.uniform(low=1.0, high=100.0, size=(100,1))
y = []

for sample in X:
	y.append(pow(sample, 0.5)/10)

X = X/np.amax(X, axis=0) 

class Neural_Network(object):
  def __init__(self):
    self.inputSize = 1
    self.outputSize = 1
    self.hiddenSize = 3
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
    self.o_delta = self.o_error*self.sigmoidPrime(o)
    self.z2_error = self.o_delta.dot(self.W2.T) 
    self.z2_delta = self.z2_error*self.sigmoidPrime(self.z2)
    self.W1 += X.T.dot(self.z2_delta) 
    self.W2 += self.z2.T.dot(self.o_delta) 

  def train (self, X, y):
    o = self.forward(X)
    self.backward(X, y, o)

NN = Neural_Network()
for i in range(1000): 
  print("Loss: \n" + str(np.mean(np.square(y - NN.forward(X)))))
  print("\n")
  NN.train(X, y)
print("INPUT: \n" + str(X*100))
print("PREDICTED OUTPUT: \n" + str(NN.forward(X)*10))