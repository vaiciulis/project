# IPND Stage 2 Final Project

# You've built a Mad-Libs game with some help from Sean.
# Now you'll work on your own game to practice your skills and demonstrate what you've learned.

# For this project, you'll be building a Fill-in-the-Blanks quiz.
# Your quiz will prompt a user with a paragraph containing several blanks.
# The user should then be asked to fill in each blank appropriately to complete the paragraph.
# This can be used as a study tool to help you remember important vocabulary!

# Note: Your game will have to accept user input so, like the Mad Libs generator,
# you won't be able to run it using Sublime's `Build` feature.
# Instead you'll need to run the program in Terminal or IDLE.
# Refer to Work Session 5 if you need a refresher on how to do this.

# To help you get started, we've provided a sample paragraph that you can use when testing your code.
# Your game should consist of 3 or more levels, so you should add your own paragraphs as well!

sample = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''

# The answer for ___1___ is 'function'. Can you figure out the others?

# We've also given you a file called fill-in-the-blanks.pyc which is a working version of the project.
# A .pyc file is a Python file that has been translated into "byte code".
# This means the code will run the same as the original .py file, but when you open it
# it won't look like Python code! But you can run it just like a regular Python file
# to see how your code should behave.

# Hint: It might help to think about how this project relates to the Mad Libs generator you built with Sean.
# In the Mad Libs generator, you take a paragraph and replace all instances of NOUN and VERB.
# How can you adapt that design to work with numbered blanks?

# If you need help, you can sign up for a 1 on 1 coaching appointment: https://calendly.com/ipnd-1-1/20min/

# HERE STARTS MY OWN CODE!!!!!!!!!!!!!!!!!!
placeholder = ['__1__', '__2__', '__3__', '__4__']

easy_fill = "I think guessing the Capital Cities of the following countries should be easy. Capital of Russia is __1__. Capital of Great Britain is __2__. Capital of France is __3__. Capital of Germany is __4__."
easy_answers = ['Moscow', 'London', 'Paris', 'Berlin']

medium_fill = "Spanish language words should be neither too easy nor too hard to fill in. Guess the following spanish words: 'Holla' translates as __1__. 'Pisso' translates as __2__. 'Mojado' translates as __3__. 'Compadre' translates as __4__"
medium_answers = ['Hello', 'floor', 'wet', 'friend']

hard_fill = "Depending on your level of Geography knowledge this might be very hard. Longest river in the world is __1__. __2__ is the World's tallest waterfall. Longest river of Lithuania is __3__. Arnold Schwarzenegger was born in the village of __4__."
hard_answers =['Nile', 'Angel Falls', 'Nemunas', 'Thal']


intro = "This quiz has three levels of difficulty. Type the level number: '1 - easy', '2 - medium' or '3 - hard'? \n"
wrong = "This is not a valid level. Would you like to try '1 - easy', '2 - medium', or '3 - hard' level? \n"



# this function asks a user to define the level of difficulty and returns it.
def level_choice(level):
	if level == "1":
		print '\n You have chosen easy level.'
		return easy_fill, easy_answers
	elif level == "2":
		print '\n You have chosen medium level.'
		return medium_fill, medium_answers
	elif level == "3":
		print '\n You have chosen hard level.'
		return hard_fill, hard_answers


# pl_string is a string in the list of placeholder.
def string_in_placeholder(pl_string,placeholder):
	for number in placeholder:
		if number in pl_string:
			return number
	return None

def substitute_pl_string(pl_string,replaced,placeholder,user_input,index):
	if string_in_placeholder(pl_string,placeholder) == None:
		if pl_string not in replaced:
			replaced.append(pl_string)
		else:
			replacement = string_in_placeholder(pl_string, placeholder)
			pl_string = pl_string.replace(replacement, user_input)
			if replacement == placeholder[index]:
				if replacement not in replaced:
					replaced.append(pl_string)
				else:
					position = replaced.index(replacement)
					replaced[position] = pl_string
			else:
				replaced.append(replacement)
	return replaced

def answers_filled(question,placeholder,replaced,user_input,index):
	split_question = question.split()
	if type(replaced) == str:
		replaced = replaced.split()
	for pl_string in split_question:
		substitute_pl_string(pl_string,replaced,placeholder,user_input,index)
	replaced = " ".join(replaced)
	return replaced

def answer_gather(level,question,answer):
	replaced =[]
	user_input = ""
	index = 0
	for number in placeholder:
		inquiry = '\nWhat will you enter instead of ' + number + '?'
		print inquiry
		user_input = raw_input()
		user_input = user_input.lower()
		while user_input not in answer[index]:
			print '\nPlease try again.'
			user_input = raw_input()
			user_input = user_input.lower()
		print '\nYour answer was correct!'
		replaced = answers_filled(question,placeholder,replaced,user_input,index)
		print replaced
		index = index + 1
	return replaced, index


def quiz():
	print 'Wellcome to the quiz!'
	level = raw_input(intro)
	if level == "1" or level == "2" or level == "3":
		question,answer = level_choice(level)
		print question
		replaced = answer_gather(level,question,answer)
		print '\nYou have completed the quiz!'
	else:
		print "\nPlease try the choices provided"
		quiz()
quiz()
