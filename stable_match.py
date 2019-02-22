
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




				


				if man_list[:women_index]:


					# moving backwards
					for _ in range(women_index-1,-1,-1):




						
						w_value=man_list[_]
						

						w_index=w_value-1


						women_list=self.women_preferences[w_index]


						w_suspect_index_in_wp=women_list.index(n+1)



						if women_list[:w_suspect_index_in_wp]:
							


							print(man_list)




							if n+1 in women_list[:w_suspect_index_in_wp]:

								print("cheated")
						else:
							break






				

			print("------")









			

	def countIt(self):
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



				








				






		
		







	



