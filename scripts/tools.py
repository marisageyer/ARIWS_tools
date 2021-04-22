import time



#def hangman():
#    name = input("What is your name? ")
#    print("Hello, " + name, "Time to play hangman!")
#    time.sleep(1)
#    print("What do you think is causing the pulsar light to dim?")
#    time.sleep(1)
#    print("Start guessing...")
#    time.sleep(0.5)
#    
#    word = "eclipse"
#    guesses = ''
#    turns = 10
#    
#    #check if the turns are more than zero
#    while turns > 0: 
#        print("\n")
#    
#        failed = 0             
#        for char in word:
#            if char in guesses:     
#                print(char,end=' ')    
#            else:
#                print("_",end=' ')    
#                # increase the failed counter with one
#                failed += 1    
#    
#        if failed == 0:        
#            print ("\n\That's right! \nNow have a look at http://www.jb.man.ac.uk/~bretonr/doublepulsar/movies/doublepulsar_eclipse.mov to learn more.")
#            break              
#        guess = input("\n\nguess a character:") 
#        guesses += guess                    
#    
#        if guess not in word:  
#         # turns counter decreases
#            turns -= 1        
#            print ("\nWrong")    
#            # how many turns are left
#            print("\nYou have", + turns, 'more guesses')
#            if turns == 0:           
#                print("\nOops! You lose! But you can try again!")



def hangman_py2():
    name = raw_input("What is your name? ")
    print "Hello, " + name, "Time to play hangman!"
    time.sleep(1)
    print "What do you think is causing the pulsar light to dim?"
    time.sleep(1)
    print "Start guessing..."
    time.sleep(0.5)
   
    word = "eclipse"
    guesses = ''
    turns = 10
   
    #check if the turns are more than zero
    while turns > 0:         
        failed = 0             
        for char in word:      
            if char in guesses:    
                print char,    
            else:
                print "_",     
                #increase the failed counter with one
                failed += 1    
   
        if failed == 0:        
            print "\nThat's right! \nNow have a look at http://www.jb.man.ac.uk/~bretonr/doublepulsar/movies/doublepulsar_eclipse.mov to learn more."  
            break              
   
        print
        guess = raw_input("guess a character:") 
        guesses += guess                    
   
        if guess not in word:  
         # turns counter decreases
            turns -= 1        
            print "Wrong"    
        # how many turns are left
            print "You have", + turns, 'more guesses' 
            if turns == 0:           
                print "Oops! You lose! But you can try again!"
   

