"""
CSSE1001 Assignment 1
Semester 2, 2020
"""

from a1_support import *

# Fill these in with your details
__author__ = "{{Haoyu Ren}} ({{46621962}})"
__email__ = "haoyu.ren@uq.net.au"
__date__ = "Aug,17,2020"



# Write your code here (i.e. functions)

def sectionA():
	"""Ask the user if they want to start the game or if they need help or if they want quit
	sectionA()->str
	"""
	print(WELCOME)
	chose = '_'
	while True:
		command1 = input(INPUT_ACTION)
		if command1 == 's':
			chose = input ("Do you want a 'FIXED' or 'ARBITRARY' length word?: ")
			#Assign a value if the format is correct
			word_select = ChoseDifficulty (chose)
			break
		elif (command1 == 'h'):
			print(HELP)
			chose = input ("Do you want a 'FIXED' or 'ARBITRARY' length word?: ")
			word_select = ChoseDifficulty (chose)
			break
		elif (command1 == 'q'):
			return None
		else:
			print(INVALID)
	return word_select

def ChoseDifficulty (chose):
	"""Check user's input word, wheather is FIXED,ARBITRARY or not
	Parameter	chose: a string by user guessed, used to compare with 'FIXED' or 'ARBITRARY'
	ChoseDifficulty(str)->str
	"""
	while True:
		if chose == 'FIXED':
			chose1 = 'FIXED'
			break
		elif chose == 'ARBITRARY':
			chose1 = 'ARBITRARY'
			break
		else:
			chose = input ("Do you want a 'FIXED' or 'ARBITRARY' length word?: ")
	return chose1
		
def select_word_at_random(word_select):
	"""The result is a collection of many words based on the words entered
	Parameter	word_select: A string representing a FIXED or ARBITRARY word selection. 
	select_word_at_random(str)->None
	"""
	if word_select == 'FIXED':
		word_select = 'FIXED'
		#get the guessed word's index：
		wordIndex = random_index(load_words(word_select))
		#get a word through the index (word is the guessed word) ：
		word = load_words(word_select)[wordIndex]
		return word
	elif word_select == 'ARBITRARY':
		word_select = 'ARBITRARY'
		wordIndex = random_index(load_words(word_select))
		word = load_words(word_select)[wordIndex]
		return word
	else:
		return None

def getLength(word):
	"""According the word from txt files to get the length
	Parameter	word: A string representing the word being guessed by the player. 
	getLength(str)->int
	"""
	# The length of be the guessed word
	word_length = len(word)
	return word_length


def tupleNumber(word_length, guess_no):
	"""get two number from a1_support's tuple which is accroding position 
	Parameter	guess no: An integer representing how many guesses the player has made
			word_length: An integer representing the length of the word being guessed by the player.
	tupleNumber(int, int)->int
	"""
	tupleNumber1 = GUESS_INDEX_TUPLE[word_length-6][guess_no-1][0] #first number
	tupleNumber2 = GUESS_INDEX_TUPLE[word_length-6][guess_no-1][1] #second number
	tupleNumber = (tupleNumber2 - tupleNumber1) +1 #since it is not include last number, so plus one
	return tupleNumber

def stepGuess(word_length, guess_no):
	"""Allows the user to make limited guesses about words
	stepGuess(int, int)->str
	"""
	tupleNumberNo = tupleNumber(word_length, guess_no)
	guess = input('Now enter Guess ' + str(guess_no) + ': ')
	while tupleNumberNo != len(guess):
		guess = input('Now enter Guess ' + str(guess_no) + ': ')
	return guess



	
def vow_or_con(guess_char):
	"""Determine the words' every char by user guessed is vowel or consonant 
	Parameter	'guess_char' is the every letter which is guessed by user
	vow_or_con(str)->int
	"""
	count = 0
	if guess_char in VOWELS:
		count = 14
	elif guess_char in CONSONANTS:
		count = 12
	return count


def compute_value_for_guess(word, start_index, end_index, guess):
	""" Through the compute to get a score after user entre a word 
	Parameter	word: A string representing the word being guessed by the player.
		 start_index, end_index are two number from a1.support tuple according the word_length
		 'guess' is a string that consisting of different Numbers of letters through user guessing.
	compute_value_for_guess(str, int, int, str)->int
	"""
	normal_scores = 5
	i1 = '' 
	i2 = ''
	count1 = 0
	count2 = 0
	count3 = 0
	word1 = word[start_index:end_index+1]
	points = 0
	#count1 and count3 are index of the words(user's guess and original word)
	#i1 and i2 is char of the words
	for count1,i1 in enumerate(guess):
		for count3,i2 in enumerate(word1):
			#when words and position are both same, user can get 14 or 12 grades 
			if i1 == i2 and count1 == count3:
				result = vow_or_con(guess[count1])   
				count2+=result
				break
			elif i1 == i2:
				count2+=normal_scores
		points = count2
	return points





def graph1(word_length):
	"""print a line:'   | 1 | 2 | 3 |...' 
	graph1(int)->None
	"""
	if word_length == 6:
		print('       '+WALL_VERTICAL+ ' 1 ' +WALL_VERTICAL+ ' 2 ' +WALL_VERTICAL+ ' 3 ' +WALL_VERTICAL+ ' 4 ' +WALL_VERTICAL+ ' 5 ' +WALL_VERTICAL+ ' 6 ' +WALL_VERTICAL)
	elif word_length == 7:
		print('       '+WALL_VERTICAL+ ' 1 ' +WALL_VERTICAL+ ' 2 ' +WALL_VERTICAL+ ' 3 ' +WALL_VERTICAL+ ' 4 ' +WALL_VERTICAL+ ' 5 ' +WALL_VERTICAL+ ' 6 ' +WALL_VERTICAL+ ' 7 ' +WALL_VERTICAL)
	elif word_length == 8:
		print('       '+WALL_VERTICAL+ ' 1 ' +WALL_VERTICAL+ ' 2 ' +WALL_VERTICAL+ ' 3 ' +WALL_VERTICAL+ ' 4 ' +WALL_VERTICAL+ ' 5 ' +WALL_VERTICAL+ ' 6 ' +WALL_VERTICAL+ ' 7 ' +WALL_VERTICAL+ ' 8 ' +WALL_VERTICAL)
	else:
		print('       '+WALL_VERTICAL+ ' 1 ' +WALL_VERTICAL+ ' 2 ' +WALL_VERTICAL+ ' 3 ' +WALL_VERTICAL+ ' 4 ' +WALL_VERTICAL+ ' 5 ' +WALL_VERTICAL+ ' 6 ' +WALL_VERTICAL+ ' 7 ' +WALL_VERTICAL+ ' 8 ' +WALL_VERTICAL+ ' 9 ' +WALL_VERTICAL)

def line(word_length):
	"""print a a divider  
	line(int)->None
	"""
	#This is a dividing line, adapted according to the length of the guessed word
	if word_length == 6:
		print('---------------------------------')
	elif word_length == 7:
		print('-------------------------------------')
	elif word_length == 8:
		print('-----------------------------------------')
	else:
		print('---------------------------------------------')


def create_guess_line(guess_no, word_length):
	"""Prompt the user for a guess, the length of the char to guess is from a1.support's tuple, 
		'*' means this position need to guess  
	create_guess_line(int, int)->list
	"""
	tupleNumber1 = GUESS_INDEX_TUPLE[word_length-6][guess_no-1][0]
	tupleNumber2 = GUESS_INDEX_TUPLE[word_length-6][guess_no-1][1]
	n = 0
	h = []#Put the entire string into a list
	h.append('Guess ')
	h.append(str(guess_no))
	#Put each new character into the List 'h'
	while n < word_length:
		if n < tupleNumber1:
			h.append(WALL_VERTICAL+' ')
			h.append(WALL_HORIZONTAL+' ')
		elif n >= tupleNumber1 and n <= tupleNumber2: #between the tuple's two number, need to guess
			h.append(WALL_VERTICAL+' ')
			h.append('*'+' ')
		else:
			h.append(WALL_VERTICAL+' ')
			h.append(WALL_HORIZONTAL+' ')
		n+=1
	h.append(WALL_VERTICAL)
	h = ''.join(h)    
	return h
	

def display_guess_matrix(guess_no, word_length, scores):
	"""Print the progress of the game, include scores every guess step
	Parameter	scores: The user's score for each guess
	display_guess_matrix(int, int, tuple)->None
	"""
	graph1(word_length)
	line(word_length)
	guess_no1 = 1
	count1 = 0
	while count1 < guess_no-1:
		print(create_guess_line(guess_no1, word_length) +'   ' + str(scores[count1]) + ' Points')
		line(word_length)
		count1+=1
		guess_no1+=1
	print(create_guess_line(guess_no1, word_length))
	line(word_length)
	

def FinalStep(word):
	"""Determine if the entire word entered by the user is correct
	FinalStep(str)->None
	"""
	guessWholeWord = input('Now enter your final guess. i.e. guess the whole word: ')
	if guessWholeWord == word:
		print('You have guessed the word correctly. Congratulations.')
	else:
		print('Your guess was wrong. The correct word was ' + '"' + word + '"')
	return None

def main():
	"""
	Handles top-level interaction with user.
	"""
	# Write the code for your main function here
	word_select = sectionA()
	if word_select == None:
		return None
	word = select_word_at_random(word_select)
	word_length = getLength(word)
	scores = ()
	print('Now try and guess the word, step by step!!')	
	graph1(word_length)
	line(word_length)
	print(create_guess_line(1, word_length))
	line(word_length)
	for guess_no in range(word_length-1):
		#start_index and end_index are element of tuple(GUESS_INDEX_TUPLE) that need to use, 
		# and changes as the guessing progresses 
		start_index = GUESS_INDEX_TUPLE[word_length-6][guess_no][0]
		end_index = GUESS_INDEX_TUPLE[word_length-6][guess_no][1]
		#'guess' is the word which is user guessed
		guess = stepGuess(word_length, guess_no+1)
		#The user's score for each guess
		grade = compute_value_for_guess(word, start_index, end_index, guess)
		scores += (grade,)
		display_guess_matrix(guess_no+2, word_length, scores)
		
	FinalStep(word) 

if __name__ == "__main__":
    main()
