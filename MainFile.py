import time
import pprint
import numpy as np
from NeuralNetwork import *
from Controler import *

X = np.random.uniform(low=1.0, high=100.0, size=(100,1))
y = []

for sample in X:
	y.append(pow(sample, 0.5)/10)

X = X/np.amax(X, axis=0) 

NN = Neural_Network()
start_time = time.time()

for i in range(1000):
  NN.loss.append(str(np.mean(np.square(y - NN.forward(X)))) + "\n")
  NN.train(X, y)

training_time = time.time() - start_time
FH = FileHandler(NN, round(training_time,3))
FH.SaveData()

print("Loss: \n" + str(np.mean(np.square(y - NN.forward(X)))))
print("INPUT: \n" + str(X*100))
print("PREDICTED OUTPUT: \n" + str(NN.forward(X)*10))