import time
import pprint
import numpy as np
from NeuralNetwork import *
from Controler import *

X = np.random.uniform(low=1.0, high=100.0, size=(100,1))
y = []

X_test = np.random.uniform(low=1.0, high=100.0, size=(100,1))
y_test = []

for sample in X:
	y.append((pow(sample, 0.5))/10)

for sample in X_test:
	y_test.append((pow(sample, 0.5))/10)

X = X/np.amax(X, axis=0)
X_test = X_test/np.amax(X_test, axis=0) 

NN = Neural_Network()
start_time = time.time()

for i in range(10000):
  NN.loss.append(str(round(np.mean(np.square(y - NN.forward(X))),4))+ "\n")
  NN.train(X, y)

training_time = time.time() - start_time
FH = FileHandler(NN, round(training_time,3))
FH.SaveData()

print("Loss: \n" + str(round(np.mean(np.square(y_test - NN.forward(X_test))),4)))
print("INPUT: \n" + str(X_test*100))
print("PREDICTED OUTPUT: \n" + str(NN.forward(X_test)*10))