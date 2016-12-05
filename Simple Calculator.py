#Hi! Thanks for viewing my code. I hope my coments are clear enough to understand...

#Reset ans to 0 for some reason
ans = 0

#We introduce the calculator and give information
def info():
    print "Welcome to my simple calculator!"
    print "Type 'fin' for your first or second number if you want to stop."
    print "This calculator does not support decimals, so just use whole numbers. Also, numbers that would end up being a fraction or decimal will appear as 0."
    print "Use 'ans' for your first or second number to substitute that number as your last answer."
    print " "
#Get started with the numbers
    num(ans)

def num(ans):
#Ask and get first number
    num1 = raw_input("First number: ")
#Check if their answer was "fin" and if it is, end the program
    if num1 == "fin":
        num2 = "fin"
        stop()
#Check if they say "ans" and if they do set their number as their last answer
    if num1 == "ans":
        num1 = ans
#Change the text with a number to an acutal number
    else:
        num1 = int(num1)
    
#Choose function
    fun = raw_input("What function? ")

#Ask and get first number + fin + ans + fix num
    num2 = raw_input("Second number: ")
    if num2 == "fin":
        stop()
    if num2 == "ans":
        num2 = ans
    else:
        num2 = int(num2)

#Find what function they said and exucate that function with their number
    if fun == "+" or fun == "plus" or fun == "add":
        ans = num1 + num2
    elif fun == "-" or fun == "minus" or fun == "subtract":
        ans = num1 - num2
    elif fun == "*" or fun == "times" or fun == "multiply":
        ans = num1 * num2
    elif fun == "/" or fun == "divide":
        ans = num1 / num2

#If something bad happens this will put the user back to the number selection
    else:
        print "ERROR"
        print " "
        print " "
        num(ans)

#Print the answer and restart
    print ans
    print " "
    print " "
    num(ans)

#If the person said "fin" earlier then we end it here
def stop():
    print " "
    print "Thanks for using my calculator!"
    raw_input(" ")


#Finally, we call the information.
info()