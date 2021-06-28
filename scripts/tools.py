import time
import os
from base64 import b64encode
from IPython.core.display import display, HTML

def time_per_bin(archive):
    time = archive.get_Integration(0).get_folding_period()
    time_per_bin = time/archive.get_nbin()
    return time_per_bin

def hangman():
    name = input("What is your name? ")
    print("\n")
    print("\nHello, " + name, "time to play hangman!")
    time.sleep(2)
    print("\n")
    print("\nWhat do you think is causing the pulsar light to dim?")
    time.sleep(1)
    print("\n")
    print("Start guessing...")
    time.sleep(0.5)
    
    word = "eclipse"
    guesses = ''
    turns = 10
    
    #check if the turns are more than zero
    while turns > 0: 
        print("\n")
    
        failed = 0             
        for char in word:
            if char in guesses:     
                print(char,end=' ')    
            else:
                print("_",end=' ')    
                # increase the failed counter with one
                failed += 1    
    
        if failed == 0:
            print("\n")        
            print("\nThat's right! The pulsar's light is dipping because of a companion passing in front of it.")
            print("\nAs you can see in this animation ... wait for it ...")
            ## display animation1
            tools_dir = '/content/drive/Shareddrives/ARIWS_timedomain/scripts'
            movfile1 = os.path.join(tools_dir,'pulsar1.mov')
            mov1 = open(movfile1,'rb').read()
            data_url = "data:video/mp4;base64," + b64encode(mov1).decode()
            display(HTML("""
            <video width=600 controls>
            <source src="%s">
            </video>
            """ % data_url))            
            print("\nAnd the companion is another pulsar!")
            print("\n")
            print("\n")
            print("\nBut to learn where these Zebra stripes come from you have to look at the details of the pulsar's magnetosphere.")
            print("\nThe magnetosphere is the plasma trapped in the closed magnetic field lines of the pulsar, and can be modelled as a doughnut-shape.")
            print("\nThis animation shows you what is going on ...")
            ## display animation2
            movfile = os.path.join(tools_dir,'pulsar.mov')
            #print(movfile)
            mov = open(movfile,'rb').read()
            data_url = "data:video/mp4;base64," + b64encode(mov).decode()
            display(HTML("""
            <video width=600 controls>
            <source src="%s">
            </video>
            """ % data_url))
            print("The movie can also be found at http://www.jb.man.ac.uk/~bretonr/doublepulsar/movies/doublepulsar_eclipse.mov")
            break              
        guess = input("\n\nguess a character: ") 
        guesses += guess                    
    
        if guess not in word:  
         # turns counter decreases
            turns -= 1        
            print ("\nWrong")    
            # how many turns are left
            print("\nYou have", + turns, 'more guesses')
            if turns == 0:           
                print("\nOops! You lose! But you can try again!")
