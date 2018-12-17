import time
import sys

class MLP_Network:
	inputData = []
	inputNumber = 0
	hiddenLayer = []
	output = 0
	trainingTime = 0
	calculatingTime = 0
	errorPercentage = 0

	def __init__(self, inputNumber):

		if inputNumber < 0:
			print("Wprowadzono liczbe ujemna!")
			sys.exit()
		else:
			self.inputNumber = inputNumber

	def Train(self):
		start_time = time.time()


		self.trainingTime = time.time() - start_time

	def Calculate(self):
		start_time = time.time()

		self.calculatingTime

		self.errorPercentage = 100 * (abs((self.inputNumber ** 2) - self.output) / self.inputNumber ** 2)

	def PrintInfo(self):
		
		print("Siec neuronowa zakonczyla nauke i wyznaczanie pierwiastka")
		print("Pierwiastek liczby ", " wedlug sieci wynosi: ", round(output, 3))
		print("Blad wzgledny to: ", round(self.errorPercentage, 3), " %")
		print("Nauka sieci trwala: ", round(self.trainingTime, 3), " s")
		print("Wyznaczanie pierwiastka trwalo: ", round(self.calculatingTime, 3), " s")
