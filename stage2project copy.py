# Stage 2 project.

placeholder = ['__1__', '__2__', '__3__', '__4__'] #list of strings to be replaced by corrrect answer.

# below are the lists of quizes and answers grouped by dificulty levels.
easy_fill = "I think guessing the Capital Cities of the following countries should be easy. Capital of Russia is __1__. Capital of Great Britain is __2__. Capital of France is __3__. Capital of Germany is __4__."
easy_answers = ['Moscow', 'London', 'Paris', 'Berlin']

medium_fill = "Spanish language words should be neither too easy nor too hard to fill in. Guess the following spanish words: 'Holla' translates as __1__. 'Pisso' translates as __2__. 'Mojado' translates as __3__. 'Compadre' translates as __4__"
medium_answers = ['Hello', 'floor', 'wet', 'friend']

hard_fill = "Depending on your level of Geography knowledge this might be very hard. Longest river in the world is __1__. __2__ is the World's tallest waterfall. Longest river of Lithuania is __3__. Arnold Schwarzenegger was born in the village of __4__."
hard_answers =['Nile', 'Angel Falls', 'Nemunas', 'Thal']


intro = "This quiz has three levels of difficulty. Type the level you would like to try: 'easy', 'medium' or 'hard'? \n"

#choosing correct set of question and answers. Input is user defined level. Output is a set of user selected level of quiz and correct answers.
def level_choice(level): 
	if level == "easy":
		print '\n You have chosen easy level.'
		return easy_fill, easy_answers
	elif level == "medium":
		print '\n You have chosen medium level.'
		return medium_fill, medium_answers
	elif level == "hard":
		print '\n You have chosen hard level.'
		return hard_fill, hard_answers





#checking if a string is in the list of 'placeholder'. Inputs are list of "placeholder" and a string in the list. Output is all the items in the list of "placeholder".
def string_in_placeholder(string,placeholder):
	for number in placeholder:
		if number in string:
			return number
	return None

#def check_answer


# this function takes in user chosen level of quiz and substitutes with correct user answers. Inputs are list of "placeholder", and user defined level set of quiz and correct answers.
def replaced_question(question, placeholder, answer):
	replaced = []
	question = question.split()
	for string in question:
		replacement = string_in_placeholder(string, placeholder)
		if replacement != None:
			user_input = raw_input("Type in the answer for: " + replacement + " ")
			#here should be a function checking if the raw_input is correct
			while user_input not in answer: # the loop to check if user answer is in the correct answer list.
				print "\nPlease try again.Your answer was wrong."
				user_input = raw_input("Type in the answer for: " + replacement + " ")
			string = string.replace(replacement, user_input)
			replaced.append(string)
			new_replaced = replaced + question[len(replaced) : ]
			joined_new = " ".join(new_replaced)
			print joined_new
		else:
			replaced.append(string)
	replaced = " ".join(replaced)
	return replaced



# main body of the quiz. Here all helper functions put together to make a final quiz.
def quiz():
	print 'Wellcome to the quiz!'
	level = raw_input(intro)
	if level == 'easy' or level == 'medium' or level == 'hard':
		question, answer = level_choice(level)
		print question
		print replaced_question(question,placeholder, answer)
		print '\nYou have successfully completed the quiz'
	else:
		print '\nThis level does not exist. Please try the choices provided!'
		quiz()
quiz()
