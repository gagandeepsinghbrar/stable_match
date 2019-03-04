
import itertools as it

class CountStableMatches():

	# Constructor takes any file name and multiple instances of this class can be spawned

	def __init__(self,filename):
		
		self.filename=filename
		

	"""
	Reads the text file and stores the numbers as lists.
	"""
	def readFile(self):

		# open file for reading with context manager so it closes it automatically later.

		with open(self.filename,"r") as inputFile:


			# get the n value as integer from first line
			self.n= int(inputFile.readline())

			# get all possible combinations.
			self.allCombinations = list(it.permutations(range(1, self.n+1)))
			
			# got men preferences and women preferences in separate lists.
			self.men_preferences=[list(map(lambda num: int(num),inputFile.readline().split(" "))) for i in range(self.n)]
			self.women_preferences=[list(map(lambda num: int(num),inputFile.readline().split(" "))) for i in range(self.n)]

			# calculate total possibilities so we can subtract later. Seems more natural eliminating.
			self.count=0

	"""

	counts the total number of stable matches
	Recieves responses one by one from isStable() on a yes or no basis
	1 means Yes and 0 means no
	adds all of them prints it


	"""
	def countTotal(self):


		for batch in self.allCombinations:

			self.count+=self.isStable(batch)


		print(self.count)
		return self.count

	"""

	Checks through all the suspects and makes sure none of them cheats


	"""
	def isStable(self,batch):


		# get indexes and values in one shot
		e=enumerate(batch)

		# start checking 
		for m,w in e:
			# m refers to men index on the top
			# w refers to the women value in the list

			# Respective men preference list that we need to worry about.
			nth_men_list = self.men_preferences[m]

			# check what is the index of his women he is married to.
			w_index_inside= nth_men_list.index(w)

			# Check his desires list. Which means slice the list from beginning excluding his current choice
			suspects=nth_men_list[:w_index_inside]

			# Only if there are any suspects. We need to investigate
			if suspects:
				# Investigation Starts : We need to check if the first suspect likes our man
				for suspect in suspects:
					# Locate where the women lives.
					women_house=self.women_preferences[suspect-1]

					# who was our man again? Oh got it ! 
					man_search=m+1

					# See where the guy who is trying to steal the girl is sitting. Got skills or nah ?
					flirt_index=women_house.index(man_search)

					# So this is the name or actual number of our fiance
					fiance_value = batch.index(suspect) + 1

					# But where is the fiance living?
					fiance_index=women_house.index(fiance_value)

					# If flirt is preferred than the fiance
					if flirt_index<fiance_index:
						# oh well, things are rough here. Nope! Not stable
						return 0
		# Look ! We reached the end. That means everyone in this batch was loyal!
		return 1





# Look dude, If you import my class this thing should not run. Only if you execute it directly.

if __name__=="__main__":
	# Let's create an instance of stable matching problem and give it an input.
	prob=CountStableMatches("input1.txt")
	# Read the file first
	prob.readFile()
	# If you got the data now, can we start now ? SMH ! What a slowpoke. We also got the value as return but 
	# who cares here , I already printed it.
	prob.countTotal()


	# Piece of cake ! 

	"""

	.
	...
	.

	...

	..

	  Just kidding....It was such a pain !


	"""

				

















				






		
		







	



