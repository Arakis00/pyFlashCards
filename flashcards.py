import csv, os, random

def flashCreate(fileName):
    '''Allows the user to create a new flash card set.'''
    #dictionary to store the values the user inputs
    cards = {}
    
    #loop until the user chooses to stop giving values
    x = True
    while x:
        #get the "side" of the card to show to the user
        print "Enter Question:"
        q = raw_input()
        #get the corresponding answer for the card
        print "Enter Answer:"
        a = raw_input()
        #saving the data to the dictionary
        cards[q] = a
        print "Do you want to add another card? (Enter y/yes or n/no)"
        again = raw_input()
        #check for exit condition
        if again.lower() == 'n' or again.lower() == 'no':
            #write dictionary to file
            fw = csv.writer(open(fileName, 'w'))
            for key, val in cards.items():
                fw.writerow([key, val])
            #print results and exit    
            print "Saved the following information you provided:"
            print cards
            x = False
            
                      
def flashStudy(fileName):
    '''Opens a flash card set that is saved to file and quizzes the user.'''
    #open file and save information to a dictionary
    fr = csv.reader(open(fileName, 'r'))
    cards = dict((rows[0],rows[1]) for rows in fr)
    #flag for running
    stillRunning = True
    
    #create and populate a dictionary to store the amount of correct answers per question/key
    correctAnswers = {}
    for key, val in cards.items():
        correctAnswers[key] = 0
    
    
    while stillRunning:        
        #run thru the dictionary and display a key then ask for the corresponding answer
        for key, val in cards.items():
            #clear screen
            os.system('cls')
            print 'Question: ', key
            print 'Enter an answer: '
            answer = raw_input()
            if answer.lower() == val.lower():
                print 'Correct!'
                #increment correct answer count based on the current key
                correctAnswers[key] = correctAnswers[key] + 1
                #remove the value from the pool if it has been answered correctly 3 times
                if correctAnswers[key] >= 3:
                    print "3rd correct guess for this question!  Removing it from the pool..."
                    del cards[key]
                    del correctAnswers[key]
            else:
                print 'Wrong!  The correct answer is: ', val
            
            #pause to let the user see the results before clearing the screen in the next iteration
            os.system("pause")
            
        if cards:
            #see if the user wants to run thru again
            print "Do you want to run thru again? (Enter n or no to exit.)"
            again = raw_input()
            if again.lower() == 'n' or again.lower() == 'no':
               stillRunning = False
        else:
            print "Out of cards..."
            stillRunning = False
            
    print "Exiting program..."
    os.system("pause")