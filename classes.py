"""This file holds all the classes necessary for Serial Box to run"""

"""This is the class that holds the definitions for all 
questions in the lesson file"""

class Question:
	"A class to hold questions"
	text = ()
	type = ()
	hint = ()
	answer = []
	
	def __init__(self, txt, typ, hnt, ans):
		self.text = txt
		self.type = typ
		self.hint = hnt
		self.answer = ans

class Lesson:
	"A class which holds all the information about the lessons"

	#Where am I?
	location = ()
	
	#Where is the music file?
	musLoc = ()

	#What questions do I have?
	questionList = [] 

	def addQuestion(self, q):
		self.questionList.append(q)
