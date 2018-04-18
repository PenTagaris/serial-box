#!/usr/bin/env python

"""This script takes an argument that should be a 
configuration file for Serial Box. 

Author: Justin Christian
Date: April 1, 2008
Language: Python
"""

import os
import sys
import classes 

def parser (lessonFileLoc):
	"""Parse a lesson file to be usable
	by Serial Box.

	Returns a Lesson class
	"""

	#instantiate a lesson class
	LessonFile = classes.Lesson()	

	#open the file
	try:
		f = open(lessonFileLoc)

		#get rid of comments, and make this file usable	
		varList = []
		for line in f:
			if line[0] != '#' and line[0] != '\n':
				varList.append(line)
			
	except IOError:
		print "File %s Not Found" % lessonFileLoc
		exit()
	

	f.close()
	LessonFile.location = lessonFileLoc

	#First thing first: the excerpt location should be the first thing
	#in the file. However, this is logical, and therefore,
	#we should not assume it is true.
	for n in range(len(varList)):
		if varList[n].find('Excerpt_Location') != -1:
			location = varList[n]
			break
		else:
			pass

	#now that we have the location of the file, 
	#get only the absolute file location
	for n in range(len(location)):
		if location[:][n].find('"') != -1:
			location = location[n+1:-2].strip() 
			break
		else:
			pass
	
	LessonFile.musLoc = location

	#now, to get the questions from the file
	qOpen = 0
	qClose = 0
	while qClose < len(varList):
		for n in range(len(varList)):
			if varList[n].find('question {') != - 1:
				qOpen = n+1
			elif varList[n].find('}') != -1:
				qClose = n
				break 

		#parse the questions now
		question = varList[qOpen:qClose]
		for line in question:
			x = line.strip().split()
			if x[0] == 'text':
				txt = line[line.find('"')+1:-2]	
			elif x[0] == 'type': 
				type = x[-1:]
			elif x[0] == 'hint':
				hint = line[line.find('"')+1:-2]
			elif x[0] == 'answer':
				ans = []
				for i in x[2:]:
					ans.append(int(i))

				
		#Make a new question
		nuQuestion = classes.Question(txt, type, hint, ans)

		#Add it to the Lesson File
		LessonFile.addQuestion(nuQuestion)
		varList = varList[qClose+1:]
	
	return LessonFile	

if __name__ == "__main__":
    # initialize a new string for the location 
    configLocation = []
    configLocation = raw_input("Config File Location: ")
    
    parser(configLocation)
