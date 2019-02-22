
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
			self.men_preferences=[list(map(lambda num: int(num),inputFile.readline().split(" "))) for i in range(self.n)]
			self.women_preferences=[list(map(lambda num: int(num),inputFile.readline().split(" "))) for i in range(self.n)]



	def countTotal(self):

		"""


		b ->  combination entire batch index ( Item number from permutations )
		n ->  combination list men value ( tricked with index )
		n+1 ->combination list real men value
		self.allCombinations[b][n] -> combination list women value
		

		"""

		for b in range(len(self.allCombinations)):


			for n in range(len(self.allCombinations[b])):


				# allCombinations[b] is tuple ( 3 4 1 2 )

				# allCombinations[b][0] is 3 the women





				# preference list for man currently [ 4 3 1 2 ]
				man_list=self.men_preferences[n]

				
				# current women 

				women=self.allCombinations[b][n]
				
				# her index in man preference 
				
				women_index=man_list.index(women)




				print(self.allCombinations[b])
				print(women_index)


				if man_list[:women_index]:






					for back_index in range(women_index,-1,-1):




						# print(man_list)
						w_value=man_list[back_index]
						 

						# home_address=self.women_preferences[man_list[women_index]-1] 
						
						


						# # target man to find in women's house
						# t=self.allCombinations[b].index(currently_checking)+1

						# if self.allCombinations[b].index(self.man_list[back_index])+1 in home_address[:home_address.index(t)]:
						# 	print("cheater")
			print("------")









			

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



				








				






		
		







	



