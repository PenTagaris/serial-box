#!/usr/bin/python

from Tkinter import *
from Image import *
from ImageTk import *
import tkMessageBox
import pitchset
from classes import *
from parser import *

class serialBox:

	def __init__(self,master,LessonFile):
		
		labelfont= ('helvetica', 14)
		buttonfont=('times', 14, 'bold')
		self.OurLessonFile = LessonFile
		frame = Frame(master)
		frame2 = Frame(frame)
		frame3 = Frame(frame)
		frame.grid()
		frame2.grid(row=2, column=1)
		frame3.grid(row=3, column=1)
		self.musloc = self.OurLessonFile.musLoc

		self.im = Image.open(self.musloc)
		self.tkimage = PhotoImage(self.im)
		self.musicImage=Label(frame, image=self.tkimage)
		self.musicImage.grid(column=1,row=0,sticky="EW")
			
		self.pitches = []
		self.states = []		
		print range(12)
		for i in range(12):
			self.var = IntVar()
			self.chk = Checkbutton(frame2, text=str(i), command=(lambda i=i: self.onPress(i)),
									variable=self.var, font=buttonfont)
			self.chk.grid(column=i,row=1)
			self.states.append(0)
		#Alright, just load everything into this init method
		#Because...well...I'm lazy. I'll fix it later.
		

        #Just Use the First Question for this Demo, fix it later
		i = 0
		
		self.primeButton = Button(frame3,text="Get Prime Form",font=buttonfont,
                                            command=self.OnPrimeButtonClick)
		self.primeButton.grid(column=0,row=4)
               
		self.vectorButton = Button(frame3,text="Get Interval Vector",font=buttonfont,
                                            command=self.OnVectorButtonClick)
		self.vectorButton.grid(column=1,row=4)

		self.inversionButton = Button(frame3,text="Get Inverted Prime Form",font=buttonfont,
                                        command=self.OnInversionClick)
		self.inversionButton.grid(column=2,row=4)
                
		self.quit = Button(frame3, text="QUIT", fg="red", command=frame.quit)
		self.quit.grid(column=1,row=7)
		self.question = Label(frame, text=self.OurLessonFile.questionList[i].text, anchor="w", font=labelfont)
		self.question.grid(column=1,row=1)
		self.answerButton = Button(frame3,text="Submit Answer!", 
											command=self.OnSubmitClick,font=buttonfont)
		self.answerButton.grid(column=1,row=2)
		self.labelVariable = StringVar()
		self.label = Label(frame3, textvariable=self.labelVariable, 
                                    anchor="center", fg="white", bg="blue", font=labelfont)
		self.label.grid(column=1,row=3)
		self.labelVariable.set(u"--Awaiting Input--")

		frame.grid_columnconfigure(0,weight=1)
		frame.update()


	def OnPrimeButtonClick(self):
		for i in range(len(self.states)):
			if self.states[i] == True:
				self.pitches.append(i)
		if (len(self.pitches)) > 0:
			self.primeForm = pitchset.printPrimeForm(self.pitches)
			self.labelVariable.set("Prime Form: " + self.primeForm)
		else:
			self.labelVariable.set("NULL")
		self.pitches=[]

	def OnVectorButtonClick(self):
		for i in range(len(self.states)):
			if self.states[i] == True:
				self.pitches.append(i)
		if (len(self.pitches)) > 0:
			self.intervalVector = pitchset.printIntervalVector(self.pitches)
			self.labelVariable.set("Interval Vector: " + self.intervalVector)
		else:
			self.labelVariable.set("NULL")
			
		self.pitches=[]

	def OnInversionClick(self):
		for i in range(len(self.states)):
			if self.states[i] == True:
				self.pitches.append(i)
		if (len(self.pitches)) > 0:
			self.primeFormInversion = pitchset.printPrimeFormInversion(self.pitches)
			self.labelVariable.set("Prime Inversion: "+ self.primeFormInversion)
		else:
			self.labelVariable.set("NULL")
			
		self.pitches = []

	def onPress(self,i):
		self.label.config(fg="white", bg="blue")
		self.labelVariable.set("--Awaiting Input--")
		self.states[i] = not self.states[i] 
		print self.states

	def OnSubmitClick(self):
		#pass
		for i in range(len(self.states)):
			if self.states[i] == True:
				self.pitches.append(i)
		if self.OurLessonFile.questionList[0].answer == self.pitches:
			print "Correct!"
			self.label.config(fg="white", bg="blue")
			self.labelVariable.set("Correct!")
		elif self.OurLessonFile.questionList[0].answer != self.pitches:
			print "Wrong!"
			self.label.config(fg="red", bg="black")
			self.labelVariable.set("WRONG!")

		self.pitches = []

def main():
	spam=raw_input('Where is the Lesson File Located?: ')
	LessonFile=parser(spam)
	root = Tk()
	root.title("Serial Box")
	app = serialBox(root,LessonFile)
	root.mainloop()

if __name__=="__main__":
	main()
