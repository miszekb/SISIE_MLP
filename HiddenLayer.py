import time
import pprint


class HiddenLayer:

	nodesNumber = 0
	inputLength = 0
	inputArray = []
	weights = []

	def __init__(self, nodesNumber, inputArray):
		self.nodesNumber = nodesNumber
		self.inputArray = inputArray
		self.inputLength = len(inputArray)

	def BuildNetwork(self):