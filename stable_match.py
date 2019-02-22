
import itertools as it

class CountStableMatches():

	def __init__(self,filename):

		self.filename=filename
		self.count=0

	def readFile(self):

		# open file for reading with context manager

		with open(self.filename,"r") as inputFile:


			# get the n value as integer
			self.n= int(inputFile.readline())

			# get all possible combinations
			self.allCombinations = list(it.permutations(range(1, self.n+1)))
			
			# got men preferences and women preferences
			self.men_preferences=[map(lambda num: int(num),inputFile.readline().split(" ")) for i in range(self.n)]
			self.women_preferences=[map(lambda num: int(num),inputFile.readline().split(" ")) for i in range(self.n)]



	def countTotal(self):

		"""


		b ->  combination entire batch index ( Item number from permutations )
		n ->  combination list men value ( tricked with index )
		n+1 ->combination list real men value
		self.allCombinations[b][n] -> combination list women value
		

		"""

		for b in range(len(self.allCombinations)):


			for n in range(len(self.allCombinations[b])):

				# start checking the man in that batch

				index_of_women_already_matched=self.men_preferences[n].index(self.allCombinations[b][n])

				print(index_of_women_already_matched)
				if self.men_preferences[n][:index_of_women_already_matched]:

					for backingUpIndex in range(index_of_women_already_matched,-1,-1):


						currently_checking=self.men_preferences[n][backingUpIndex]

						home_address=self.women_preferences[self.men_preferences[n][index_of_women_already_matched]-1] 
						
						


						# target man to find in women's house
						t=self.allCombinations[b].index(currently_checking)+1

						if self.allCombinations[b].index(self.men_preferences[n][backingUpIndex])+1 in home_address[:home_address.index(t)]:
							print("cheater")










			

	def checkIfValid(self):
		pass


				



if __name__=="__main__":
	prob=CountStableMatches("input1.txt")
	prob.readFile()
	prob.countTotal()










# for batchNo in range(len(allCombinations)):
	
# 	# looping over that particular combination

# 	for n in range(len(allCombinations[batchNo])):



		
		
# 		i_of_women=men_preferences[n].index(allCombinations[batchNo][n])
# 		# n[:i] gives cheaters on the left
# 		if men_preferences[n][:i_of_women]:

# 			for jump in range(i_of_women,-1,-1):

# 				# men_preferences[n][jump]-1   -> index of suspected women
# 				#allCombinations[batchNo].index(men_preferences[n][jump])+1 -> who is she matched with



				








				






		
		







	



