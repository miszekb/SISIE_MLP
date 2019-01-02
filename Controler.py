import time
import pprint
import numpy as np

class FileHandler:

	network = 0
	time = 0

	def __init__ (self, network, train_time):

		self.network = network
		self.train_time = train_time

	def SaveData(self):
		lossFile = open("loss", "w")
		timeFile = open("time", "w")

		for x in self.network.loss:
			lossFile.write(x)

		timeFile.write(str(self.train_time))

		lossFile.close()
		timeFile.close()


		


		


