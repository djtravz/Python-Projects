def start():
    print "Welcome to my countdown thingy!"
    print "All you have to do to use my program is type in a number when it asks for it and it will count down from your number to what specify by what increment you specify."
    print "Lets begin, shall we?"
    print " "
    num()
def num():
    strt = raw_input("What is your starting number?")
    strt = int(strt)
    print " "
    
    incr = raw_input("By what increment should it decrease?")
    incr = int(incr)
    print " "
    
    end = raw_input("What is your ending number?")
    end = int(end)
    
    print " "
    cur = strt
    begin(cur,incr,end)
def begin(cur,incr,end):
    print cur
    cur = cur - incr
    if cur == end:
        print end
        stop()
    else:
        begin(cur,incr,end)
def stop():
    print " "
    print " "
    print "Done!"
    print " "
    ans = raw_input("Would you like to do it again? (y or n)")
    if ans == "y":
        print "Starting again!"
        print " "
        print " "
        num()
    elif ans == "n":
        print "Sad to see you go!"
        print "Goodbye!"
        raw_input(" ")
    else:
        raw_input("ERROR! PRESS ENTER")
start()