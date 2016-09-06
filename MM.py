def start():
	print "INITIATING... Done!"
	print " "
	print "Welcome to Mythology Mission!"
	print "In MM you can't choose your path, but you can still select what you think the actual myth is."
	print "If you fail to go by the myth you will be reset back to the start of your decision."
	print "Let's go!"
	skip = raw_input("Press enter to start! ")
	if skip == "skip":
		stop()
	else:
		des1()
def des1():
	print " "
	print " "
	print "Currently, you are playing the role of King Acrisius"
	print " "
	print "The oracle of Delphi has just told you that your daughter, Danae, will have a child and that child will kill you."
	ans = raw_input("Do you (1) lock her in a bronze tower or (2) let her be and encourage her to have a child? ")
	if ans == "1":
		print "Correct answer!"
		print "You lock her in a bronze tower."
		des2()
	elif ans == "2":
		print "Wrong! Your grandson will just kill you eventually!"
		des1()
	elif ans == "skip":
		stop()
	else:
		"ERROR 404! Answer not found!!"
		des1()
def des2():
	print " "
	print " "
	print "Currently, you are playing the role of the god Zeus."
	print " "
	print "Danae is feeling depressed and bored in her tower."
	ans = raw_input("Do you (1) go into the tower and make her happy or (2) leave her alone and let her eventually kill herself? ")
	if ans == "1":
		print "Correct answer!"
		print "You also make her boring prison very beautiful."
		des3()
	elif ans == "2":
		print "Wrong! Making people happy is the best!"
		des2()
	elif ans == "skip":
		stop()
	else:
		print "ERROR 404! Answer not found!!"
		des2()
def des3():
	print " "
	print " "
	print "You are now playing the role of King Acrisius."
	print " "
	print "A while later Danae has a child which she names Perseus. You find out and you are furious."
	ans = raw_input("Do you (1) do nothing or (2) put Danae and baby Perseus in a chest and cast them out to sea? ")
	if ans == "1":
		print "Wrong! Perseus will kill you. You must do anything and everything in your power to stop him."
		des3()
	elif ans == "2":
		print "Correct answer!"
		print "You cast them out to sea."
		des5()
	elif ans == "skip":
		stop()
	else:
		print "ERROR 404! Answer not found!!"
		des3()
#Skip 4 because I forgot
def des5():
	print " "
	print " "
	print "Currently, you are playing the role of Dictys, the King of Seriphos' brother."
	print " "
	print "The chest manages to drift across the ocean and eventually come to the shore of the island of Seriphos."
	ans = raw_input("Do you (1) let the chest drift away from Seriphos or (2) pick up the chest and see what is inside? ")
	if ans == "1":
		print "Wrong! You want to see what is inside the chest!"
		des5()
	if ans == "2":
		print "Correct answer!"
		print "You open the chest and you see Danae and young Perseus"
		des6()
	elif ans == "skip":
		stop()
	else:
		print "ERROR 404! Answer not found!!"
		des5()
def des6():
	print " "
	print " "
	print "Currently, you are playing the role of Polydectes, the King of Seriphos."
	print " "
	print "Perseus is becoming a very well trained young man and you realize that Danae doesn't have a spouse."
	ans = raw_input("Do you (1) ask for her hand in marriage or (2) kidnap Perseus and treat him as your own? ")
	if ans == "2":
		print "No! Just no."
		des6()
	if ans == "1":
		print "Correct answer, but Danae rejects you. You must come up with a complicated plan to marry her by not using force."
		des7_stry()
	elif ans == "skip":
		stop()
	else:
		print "ERROR 404! Answer not found!!"
		des6()
def des7_stry():
	print " "
	print "You pretend to marry the daughter of your good friend. Everybody had to bring a wedding present, including Perseus."
	print "However, Perseus, being poor, had not brought anything, and you pretend to be furious. After a heated discussion, Perseus said he would bring you anything for which you would ask."
	print "So, you ask for the head of the Gorgon Medusa."
	med()
	des7()
def des7():
	print " "
	print " "
	print "You are now playing the role of Perseus, the Hero of this story."
	print " "
	print "You set forth on your adventure. After wondering for days searching for the Gorgon's lair. You are beginning to feel hopeless. "
	ans = raw_input("Do you (1) continue or (2) give up? ")
	if ans == "2":
		print "Wrong! You must complete your quest."
		des7()
	if ans == "1":
		print "Correct answer!"
		print "You continue searching for the lair."
		des8()
	elif ans == "skip":
		stop()
	else:
		print "ERROR 404! Answer not found!!"
		des7()
def des8():
	print " "
	print " "
	print "In your despair you come across a tall woman and a young man with winged sandals. They identify themselves as goddess Athena and god Hermes."
	ans = raw_input("Do you (1) disregard them or (2) believe what they say? ")
	if ans == "1":
		print "Wrong! They are the real deal."
		des8()
	elif ans == "2":
		print "Correct answer!"
		print "You believe what they say and they help you with your quest. Hermes gives you his winged sandals and his staff to kill Medusa. Athena gives you her shield. It will be helpful because you won't have to risk looking into Medusa's eyes."
		des9_stry()
	elif ans == "skip":
		stop()
	else:
		print "ERROR 404! Answer not found!!"
		des8()
def des9_stry():
	print " "
	print "After getting these two items you eventually go to the lair of Medusa and her sisters, who you find are sleeping. You manage to kill Medusa using the sickle. "
	print "On your way back to Seriphus you have many adventures (which we are not going into now). Some of them include meeting the Titan Atlas, who was condemned to carry the heavens on his shoulders, and helping Andromeda who was chained to a rock. You become friends with Andromeda and you set off for Seriphus together."
	des9()
def des9():
	print " "
	print " "
	print "On your way home you stop at Larisa, so you can compete in some games that were held at the time. "
	ans = raw_input("In the discus competition do you (1) use all of your strength or (2) barely throw it? ")
	if ans == "1":
		print "You use all of your strength while throwing it and manage to kill your grandfather."
		print "This fulfills the prophecy. Good job."
		end()
	elif ans == "2":
		print "You barely throw it and the wind whips it up and you manage to kill your grandfather."
		print "This fulfills the prophecy. Good job."
		end()
	elif ans == "skip":
		stop()
	else:
		print "ERROR 404! Answer not found!!"
		des9()
def end():
	print " "
	print "You set off at morning to go home."
	print "When you arrived at Seriphus, the first person you meet is Dictys, the fisherman who had brought you and Danae ashore many years ago. Dictys tells you how Polydectes had never really married, but since Danae wouldn't marry Polydectes, he forced her to be his handmaiden." 
	print "You are furious, so you ask Dictys to take care of Andromeda, in order to avenge your mother's mistreatment. "
	print "You storm to the palace, walk in and say, 'Let all who are my friends shield their eyes!' After saying this you raised Medusa's head and Polydectes and his courtiers were immediately turned to stone. You and Andromeda lived happily for many years and your descendants became great kings, the greatest of them all being Hercules, the strongest man in the world."
	print " "
	print " "
	print "Eventually, Perseus was killed by Dionysus. To be immortalized, Perseus and Andromeda were turned into stars and would live together in the sky."
	endend()
def endend():
	print " "
	print " "
	print "You are now playing the role of yourself."
	print " "
	ans = raw_input("Thanks for playing Mythology Mission! Would you like to play again? (y or n) ")
	if ans == "y":
		print " "
		print "OK! Let's start anew!"
		print " "
		print " "
		print " "
		start()
	elif ans == "n":
		print " "
		print "Alrighty then! :)"
		stop()
	elif ans == "skip":
		stop()
	else:
		print "ERROR 404! Answer not found!!"
		endend()
def med():
	print " "
	print "Medusa was a horrible creature, who had snakes growing out of her head instead of hair, and a terrifying gaze that literary petrified anyone who would look into her eyes."
	print " "
def stop():
	print " "
	smile()
def smile():
	import turtle
	import Tkinter
	smiles = turtle.Turtle()    
	smiles.penup()
	smiles.goto(-75,150)
	smiles.pendown()
	smiles.circle(10)
	smiles.penup()
	smiles.goto(75,150)
	smiles.pendown()
	smiles.circle(10)
	smiles.penup()
	smiles.goto(0,0)
	smiles.pendown()
	smiles.circle(100,90)
	smiles.penup()           
	smiles.setheading(180)
	smiles.goto(0,0)
	smiles.pendown()
	smiles.circle(-100,90)
	raw_input("")
def bleh():
	raw_input(" ")
#Start! (Obviously)
start()