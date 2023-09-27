# Mastermind game by Landy Ko 20043923

# Define start() function to display the main page
# Options 1, 2, or 3 for user to choose
# .center() returns centered in a string of length width
def start():

    print(80*'=')
    print('WELCOME TO MASTERMIND'.center(80))
    print(80*'=')
    print('\n1. Play game \n2. How to play \n3. Quit')
    print('\nEnter 1, 2, or 3')

    try: 
        option = int(input('Option : ').strip())

    except ValueError:
         print("That's not a number! Please re-enter.")
         start()
    
    # Output based on the user input 
    if option == 1:
         game()

    elif option == 2:
         help()
         start()

    elif option == 3:
         endgame()

    else:
         print('\nEnter only 1 / 2 / 3.\n')
         start()

# Define help() function to display a guideline for user 
def help():
    print(80*'=')
    print('HOW TO PLAY'.center(80))
    print(80*'=')
    print('\n')
    print('1. The system will randomly generate four colours in an order.')
    print('2. You are required to input your guess.')
    print('3. The system will give you a feedback based on your guess. For example:\n')
    print('Correct colours in the correct place  : 1'.center(80))
    print('Correct colours but in the wrong place: 3'.center(80))
    print('\n4. The game will end if your guess matches with the randomized colours')
    print('   and show the total number of guess(es) you took.')
    print('5. If not, the system will prompt you to enter another guess.')
    print('6. Please be reminded that you only have 10 chances.')
    print('\n')

# Define endgame() function to terminate program
def endgame():
    print(80*'=')
    print('END'.center(80))
    print(80*'=')
    quit()

# Define results(correct_place, wrong_place) function to show feedback on
# correct colours in correct place and
# correct colours but in the wrong place
def results(correct_place, wrong_place):
    print("\nCorrect colours in the correct place  : ", correct_place)
    print("Correct colours but in the wrong place: ", wrong_place) 


# Define game() function to start the Mastermind gane
def game():
    print(80*'=')
    print('START GAME'.center(80))
    print(80*'=')

    import random    # Import a random module to generate a sequence of four colours  

    #List containing 4 colours to be randomized from
    colourList=['red', 'yellow', 'blue', 'green']
    print('\nType red / yellow / blue / green for your input.\n') 

    count = 0         # To assign initial attempt at 0   
    answerList=[]     # A list containing the randomized colours
    userList=[]       # A list containing the user's input
    game1 = True
          
    # Randomly generate four colours
    for i in range(4):
         answerList.append(random.choice(colourList))
      
    while game1:
          count +=1    # count increases one indicates number of attempts increases one
          
          # Get input from user
          # .lower() converting the input into lower case
          # .strip() removes spaces at the beginning and
          # end of the string 
          while len(userList)!= 4:
                guess=str((input('\nChoice of color:')).strip()).lower()
                
                # Input validation to check whether user input a correct colour
                if guess not in colourList:     
                    print(80*'-')   
                    print('\n\t   ERROR ! Type a valid colour based on the instructions given!\n')
                    print(80*'-')
                else:
                    userList.append(guess)     # Append the input into a list 
          
          # Loop to calculate correct_place and wrong_place
          q=0 
          correct_place=0
          
          while q < len(userList):
              if userList[q] == answerList[q]:
                   correct_place += 1             
              q += 1

          # Copy the userList and answerList to another two temporary list
          # for further checking 
          userList_tempo = userList.copy()
          answerList_tempo = answerList.copy()

          # Removing the correct colours in the correct place from temporary list 
          t=0
          while t < len(userList):
               if userList[t] in answerList and userList[t] == answerList[t]:
                    userList_tempo.remove(userList[t])       
                    answerList_tempo.remove(answerList[t])               
               t += 1

          # If the colour from the temporary userList is in the temporary answerList
          # this consider correct colour but in the wrong place
          j=0
          wrong_place = 0
          while  j < len(userList_tempo):
                 if userList_tempo[j] in answerList_tempo:
                      wrong_place +=1
                 j+=1

          # Output
          if userList == answerList:
               results(correct_place, wrong_place)

               # If user win at the first attempt
               if count ==1 :
                    print('\n')
                    print(80*'=')
                    print('*** WELL DONE ***'.center(80))
                    print('\n')           
                    print('\t\t   Congratulations! You took only 1 guess !')
                    print(80*'=')

               # If user win after taking a few attempts 
               else :
                    print('\n')
                    print(80*'=')
                    print('*** WELL DONE ***'.center(80))
                    print('\n')           
                    print('\t\t\tCongratulations! You took', count, 'guess(es)!')
                    print(80*'=')
               game1=False
               
          # If user exceed 10 attempts 
          elif count >=10:       
                  print('\n\nYou came to the limit! The answer is', answerList,'\n')
                  game1=False
                  
          # If user took a wrong guess, prompt user to make another guess 
          else:
              results(correct_place, wrong_place)
              userList=[]
          
          # User can choose to replay the game
          # .upper() convert the input to capital letter
          # quit() function to exit the program
          while game1 == False:
                print('\n')
                print('*** REPLAY ***'.center(80))
                repeat_game = input('\nDo you want to play again (Y/N)? : ').upper()
                print('\n')

                # If user types N, run endgame() function
                # Exit the program
                if repeat_game =="N":
                     endgame()
                     quit()

                # If user types Y, run game() function 
                elif repeat_game == "Y":
                     game()

                else:
                     print(80*'-')   
                     print('\n\t\t\tPlease enter a valid input !\n')
                     print(80*'-')
                     game1 = False
                        
# Calling the function
start()
