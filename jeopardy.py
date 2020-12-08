import RPi.GPIO as GPIO
from gpiozero import LED
from keyboard import is_pressed
from csv import reader
from time import sleep
from random import shuffle, random

def initialize():
	file = open('jQuestion.csv')
	questions = file.readlines()
	file.close()

	file = open('jAnswer.csv')
	answers = file.readlines()
	file.close()
	
	return questions, answers

def welcome():
	print("\nWELCOME TO JEOPARDY!")
	sleep(4)
	print("Here is how to play:")
	sleep(2)
	print("Divide yourselves into 2 teams.")
	sleep(3)
	print("Get points by answering True or False Questions. Hold down the button after 3 seconds to answer 'True', else, the answer is 'False'")
	sleep(4)
	print("The first team to get 4 points wins the game!")
	sleep(5)
	print("\n"*100)
	print("Start!")
	sleep(1)

def scores(teams):
	if teams[0] > teams[1]:
		print('Blue Wins!')
		print(teams)
	elif teams[0] < teams[1]:
		print('Yellow Wins!')
		print(teams)
	elif teams[0] == teams[1]:
		print('Tie...')
		print(teams)

def pointCol(teams):
	if teams == [0,0]:
		b1.off()
		b2.off()
		b3.off()
		b4.off()
		y1.off()
		y2.off()
		y3.off()
		y4.off()

	if teams[0] == 1:
		b1.on()
	if teams[0] == 2:
		b1.on()
		b2.on()
	if teams[0] == 3:
		b1.on()
		b2.on()
		b3.on()
	if teams[0] == 4:
		b1.on()
		b2.on()
		b3.on()
		b4.on()

	if teams[1] == 1:
		y1.on()
	if teams[1] == 2:
		y1.on()
		y2.on()
	if teams[1] == 3:
		y1.on()
		y2.on()
		y3.on()
	if teams[1] == 4:
		y1.on()
		y2.on()
		y3.on()
		y4.on()

def wave():
	for row in range(10):
		sleep(0.1)
		b1.on()
		y1.off()
		sleep(0.1)
		b2.on()
		y2.off()
		sleep(0.1)
		b1.off()
		b3.on()
		sleep(0.1)
		b2.off()
		b4.on()
		sleep(0.1)
		b3.off()
		y4.on()
		sleep(0.1)
		y3.on()
		b4.off()
		sleep(0.1)
		y2.on()
		y4.off()
		sleep(0.1)
		y1.on()
		y3.off()
	y2.off()
	y1.off()

def countdown():
	b1.on()
	b2.on()
	b3.on()
	b4.on()
	y1.on()
	y2.on()
	y3.on()
	y4.on()
	print('\n'*100+questions[row]+'\n'+'5')
	sleep(1)
	print('\n'*100+questions[row]+'\n'+'4')
	b4.off()
	y4.off()
	sleep(1)
	print('\n'*100+questions[row]+'\n'+'3')
	b3.off()
	y3.off()
	sleep(1)
	print('\n'*100+questions[row]+'\n'+'2')
	b2.off()
	y2.off()
	sleep(1)
	print('\n'*100+questions[row]+'\n'+'1')
	b1.off()
	y1.off()
	sleep(1)

def randomizer():
  return ranNum

b1 = LED(22)
b2 = LED(27)
b3 = LED(17)
b4 = LED(4)

y1 = LED(25)
y2 = LED(24)
y3 = LED(23)
y4 = LED(18)

GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN)

#welcome()
path = 'p'
while path != 'e':
	path = raw_input(str('Play(p) or Exit(e)?\n - '))
	ranNum = random()
	questions, answers = initialize()
	shuffle(questions, randomizer), shuffle(answers, randomizer)
	teams = [0,0]
	pointCol(teams)
	ps = 0

	for row in range(len(questions)):
		print('\n'*100+'Get Ready!')
		sleep(5)
		print(questions[row])
		countdown()

		if GPIO.input(26) == 0:
			ans = "True\r\n"
		else:
			ans = "False\r\n"

		wave()
		
		if answers[row] == ans:
			print('\n'*100+'Correct!\n')

			if row%2 == 0:
				teams[0] += 1
			else:
				teams[1] += 1

		elif answers[row] != ans:
			print('\n'*100+'Wrong!\n')

		sleep(1)
		pointCol(teams)
		sleep(1)

		if ps == 1 and (teams[0] >= 4 or teams[1] >= 4):
			print('\n')
			break

		if teams[0] == 4:
			ps = 1

		
	print("\n")
	scores(teams)
	print("\n")
