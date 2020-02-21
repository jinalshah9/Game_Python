#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
Doc String:
    A) Introduction:
           This game takes a contestant through a jungle survival experience.
           The contestant has to face 3 levels of difficulties.
           No knowledge or skills are required.
           This game is purely based on luck
           
           1) Tragedy 1: EAT A FRUIT OR NOT
                         Whether the fruit is poisonous or not depends on your luck.
                         Contestant gets 2 attempts
                         
                         Inspired from – “Snow White” story
                         
           2) Tragedy 2: ENCOUNTER WITH RANDOM WILD ANIMAL
                         Whether the wild animal attacks you or not depends on your luck.
                         Contestant gets 2 attempts only if there is an invalid entry
                         
                         Inspired from – “The Two friends and the Bear” story
                         
           3) Tragedy 3: CROSS THE RIVER OR WAIT FOR FOREST OFFICIALS TO RESCUE
                         Whether you win or lose depends on your luck.
                         Contestant gets 2 attempts.
                         
                         Inspired from – “Camp or walk in a plane crash” case

            
    B) Known Errors and/or Bugs:
            None

"""



from sys import exit
import random
from random import randint
import time

def game_start() :
    global contestant_name
    global favourite_fruit
    global swim_status
    
    
    print(f'Hello and welcome to THE TRAGEDY GAMESHOW!!!\n')
    input('<Press Enter key to continue>\n')
    print(f'Yes! its the \'OH I GOT LOST IN THE JUNGLE\' episode again...')
    print(f'And I am your same old host JINAAAAAAAAAAAAL.....')
    input('<Press Enter key to continue>\n')
    
    print(f'Let\'s call on stage our contestant to walk us through a very scary night in the jungle...')
    print(f'Ooooooooooo.....!!!!')
    time.sleep(2)
    print("\nRound of applause for our contestant")
    input('<Press Enter key to welcome the contestant>\n')
    
    #Input global variables
    #The input variables for now are not made mandatory
    #Input of sentences like "My name is Mr. XYZ" will affect the story grammatically as well
    
    contestant_name = input('What\'s your name contestant? <Please enter your first name> :\t')
    contestant_name = contestant_name.capitalize()
    print(f'\nWelcome to the game, {contestant_name}!! Tell us something about you..\n')
    
    input('\nWhere are you from? <Please enter your country> :\t')
    favourite_fruit = input('What\'s your favourite fruit? <Please enter your favorite fruit> :\t')
    favourite_fruit = favourite_fruit.lower()
    input('Are you scared of height? <Please enter yes or no> :\t')
    input('Are you scared of darkness? <Please enter yes or no> :\t')
    swim_status = input('Do you know to swim? <Please enter yes or no> :\t')
    swim_status = swim_status.lower()
    
    print(f'\nSo now we know so much about you, {contestant_name}..')
    print(f'As you know we give you an imaginary situation of being stuck in a jungle and you have to escape each difficulty level...')
    time.sleep(1)
    print(f'\nLet\'s begin with our game..')
    input('<Press Enter key to continue>\n')
    print(f"{'-' * 120}")
    time.sleep(1)
    print(f'\nYou were driving through a \'forest highway\' and your car broke down...')
    print(f'You look around for help but the roads are dead...')
    input('<Press Enter key to continue>\n')
    
    #little narration to make the story interesting
    print(f'You inform the forest officials about your situation... They ask you to somehow make your way to the nearby river..')
    time.sleep(2)
    print(f'\nYou are scared but decide to keep your spirits high..!!')
    time.sleep(1)
    print(f'\nYou slowly gather the courage to walk inside the jungle...')
    input('<Press Enter key to continue>\n')
    print(f"\nLight man? This was your cue to dim the light...")
    input('<Press Enter key to continue>\n')
    
    #Just a count down before we begin the first round
    loop = 3
    while loop > 0:
        print(loop)
        time.sleep(1)
        loop -= 1
    tragedy_1()
    
def tragedy_1() :
    print(f"{'-' * 120}")
    time.sleep(1)
    print(f"""
  _                   _   _ 
 | |    _____   _____| | / |
 | |   / _ \ \ / / _ \ | | |
 | |__|  __/\ V /  __/ | | |
 |_____\___| \_/ \___|_| |_|
                            
    
""")
    input('<Press Enter key to continue>\n')
    print(f'\nAs you enter the jungle {contestant_name}, you walk through these beautiful trees... You are extremely hungry...')
    time.sleep(2)
    print(f'\nSuddenly you notice this delicious looking fruit..')
    print(f'It actually reminded you of your favourite fruit, {favourite_fruit}...')
    time.sleep(1)
    input('<Press Enter key to continue>\n')
    print(f'\nRemember you need energy to survive in this jungle.. But don\'t forget that the fruit could be poisonous...')
    time.sleep(1)
    print(f'\nNow is your chance to decide whether you eat the fruit or not...')    
    input('<Press Enter key whenever you are ready>\n')
    
    loop1 = 2
    
    while loop1 > 0:
        poisonous_value = randint(1,2)
        poisonous_value = str(poisonous_value)
        
        #poisonous value 1 means that the fruit is not poisonous and poisonous value 2 means that the fruit is poisonous
        
        poisonous_status = ()
        if poisonous_value == "1":
            poisonous_status = "not poisonous"
        else:
            poisonous_status = "poisonous"
        
        print(f"""
So {contestant_name}, what\'s your decision?
Option 1 : If you want to eat the fruit then type 1
Option 2 : If you don't want to eat the fruit then type 2

""")
        
        decision1 = input('<Enter 1 or 2 as per your decision:>\t')
        
        #The entry should only be 1 or 2
        if decision1 == "1" or decision1 == "2":
          
            #if you eat the fruit (decision1 is "1") and the fruit is not poisonous (poisonous_value is "1") then you go to the next level
            #Also, if you don't eat the fruit (decision1 is "2") and the fruit is poisonous (poisonous_value is "2") then you go to the next level
            if decision1 == poisonous_value:
                print(f'\n\nHurray! You took the right decision.. The fruit was {poisonous_status}... Let\'s move forward...\n')
                input('<Press Enter key to continue>\n')
                tragedy_2()
                break
            
            #if the above condition is not true and this is your last chance to guess
            elif loop1 == 1:
                print(f'\nOh no {contestant_name}, that\'s not a good decision.. The fruit was {poisonous_status}...\n')
            
            #if the first sub-condition is not true but you have one more chance to guess
            else:
                print(f'\nOops! That\'s not a good decision...\n')
                print(f"{'-' * 120}")

        else:
            print("\nInvalid entry.. The accepted entry is either 1 or 2..\n")
            print(f"{'-' * 120}")
        
        loop1 -= 1
    fail()
    

def tragedy_2() :
    global animal_encounter
    
    print(f"{'-' * 120}")
    print(f"""
  _                   _   ____  
 | |    _____   _____| | |___ \ 
 | |   / _ \ \ / / _ \ |   __) |
 | |__|  __/\ V /  __/ |  / __/ 
 |_____\___| \_/ \___|_| |_____|
                                
    
""")
    input('<Press Enter key to continue>\n')
    animal_list = ["roaring bear", "growling leopard", "hungry tiger"]
    animal_encounter = random.choice(animal_list)
    
    print(f'As you further walk in the jungle trying to find the river, you see a {animal_encounter}...')
    input('<Press Enter key to continue>\n')
          
    print(f'\nYou almost freeze in your place... The {animal_encounter} is looking straight at you...')
    time.sleep(1)
    print(f'\n{contestant_name}, you see a small hiding spot nearby... but you could also act dead..')
    
    time.sleep(2)
    
    print(f'\nYou have to decide really fast about what you want to do next...')
    input('<Press Enter key whenever you are ready>\n')
          
    loop2 = 2
    while loop2 > 0:
          print(f"""
You have 3 options to decide from:

Option 1 : If you want to run to the hiding spot then type 1
Option 2 : If you want to act dead then type 2
Option 3 : If you are unable to decide and just stand there then type 3

So {contestant_name}, what's your decision?

""")
          decision2 = input('<Enter 1, 2 or 3 as per your decision:>\t')
          
          if decision2 == "1" or decision2 == "2" or decision2 == "3":
              input('<Press enter to continue>')
              
              attack_value = randint(1,2)
              #attack_value 1 means that the animal attacks you & you die while attack_value 2 means that the animal walks away
              #irrespective of your decision if attack_value is 1 then you lose the game
              
              if attack_value == 1:
                  print(f'\nOhhhh noooooo, {contestant_name}.... The {animal_encounter} attacked you..')
                  fail()
                  break
              else:
                  print(f'\nLooks like luck is totally in your favor today, {contestant_name}...')
                  print(f'The {animal_encounter} heard some noise from the opposite direction and walked away....')
                  time.sleep(2)
                  print(f'\nYou can take a sigh of relief before we move to the next step..')
                  input('<Press Enter key to continue>\n')
                  tragedy_3()
                  break  
          
          #only if you enter an invalid entry then you get another chance to type correctly
          else:
            print('\nInvalid Entry..!! The accepted entry is either 1, 2 or 3..!!\n')
            print(f"{'-' * 120}")
            loop2 -= 1
    fail()
    


def tragedy_3() :
    print(f"\n{'-' * 120}")
    print(f"""
  _____ _             _   _                   _ 
 |  ___(_)_ __   __ _| | | |    _____   _____| |
 | |_  | | '_ \ / _` | | | |   / _ \ \ / / _ \ |
 |  _| | | | | | (_| | | | |__|  __/\ V /  __/ |
 |_|   |_|_| |_|\__,_|_| |_____\___| \_/ \___|_|                                    

""")
    input('<Press Enter key to continue>')
    print(f'\n{contestant_name}, now this is the last level of our difficulty in the jungle....')
    time.sleep(2)
    print(f'\n\nAfter dealing with the {animal_encounter}, you realise that the river is very nearby..')
    print(f'You follow the trails of animals that you notice and find the river...')
    time.sleep(2)
    print(f'\n\nIts time to make a final decision {contestant_name}, and see if you survive the JUNGLEEEEE.....')
    input('<Press Enter key whenever you are ready>\n')
    
    loop3 = 2
    while loop3 > 0:
        cross_over = random.randint(0,1)
        #cross_over 0 means that you cross the river successfully while cross_over 1 means that you are unable to cross the river
          
        get_rescued = random.randint(0,1)
        #get_rescued 0 means that the forest officials rescue you while get_rescued 1 means that the forest officials are unable to rescue you
                   
        print(f"""
So {contestant_name}, what\'s your decision?
Option 1 : If you want to cross the river then type 1
Option 2 : If you want to wait at the river bank for the forest officials to rescue you then type 2

""")
        decision3 = input('<Enter 1 or 2 as per your decision:>\t')
        if decision3 == "1":
            
            #if you don't know to swim and you decide to cross the river then you fail
            if 'n' in swim_status or 'no' in swim_status:
                print(f'\nWait {contestant_name}, did you forget that you can\'t swim?')
                time.sleep(1)
                print(f'You tried your best but couldn\'t swim across the river...')
                fail()
                break
          
            #below 3 conditions within decision3 as 1 are applicable when you enter anything but [no,n] for swim_status
            #if cross_over is 0 then you win
            elif cross_over == 0:
                print(f'\nHurray!! Awesome decision, {contestant_name}...')
                print(f"""
 __   _____  _   _  __        _____ _   _    _   _    
 \ \ / / _ \| | | | \ \      / /_ _| \ | |  | | | |   
  \ V / | | | | | |  \ \ /\ / / | ||  \| |  | | | |   
   | || |_| | |_| |   \ V  V /  | || |\  |  |_| |_|   
   |_| \___/ \___/     \_/\_/  |___|_| \_|  (_) (_)                 

""")
                input('<Press Enter key to exit>\n')
                game_over()
                break
                
            #if cross_over is 1 and its your last chance
            elif loop3 == 1:
                print(f'\nOhhhh {contestant_name}, the rapids were large and so you couldn\'t cross the river')
            
            #if cross_over is 1 but you have 1 chance left
            else:
                print(f'\nThis is not a wise decision.. TRY AGAIN...\n')
                print(f"{'-' * 120}")
        
        elif decision3 == "2":
            if get_rescued == 0:
                print(f'\nHurray!! Awesome decision, {contestant_name}... You were rescued by the forest officials..')
                print(f"""
 __   _____  _   _  __        _____ _   _    _   _    
 \ \ / / _ \| | | | \ \      / /_ _| \ | |  | | | |   
  \ V / | | | | | |  \ \ /\ / / | ||  \| |  | | | |   
   | || |_| | |_| |   \ V  V /  | || |\  |  |_| |_|   
   |_| \___/ \___/     \_/\_/  |___|_| \_|  (_) (_)                 

""")
                input('<Press Enter key to exit>\n')
                game_over()
                break
                
            #if get_rescued is 1 and its your last chance
            elif loop3 == 1:
                print(f'\nOhhhh {contestant_name}, unfortunately some animal attacked you before the forest officials could reach you..')
            
            #if get_rescued is 1 but you have 1 chance left
            else:
                print(f'\nThis was not a wise decision.. TRY AGAIN...\n')
                print(f"{'-' * 120}")
        
        else:
            print('\nInvalid Entry..!! The accepted entry is either 1 or 2..!!\n')
            print(f"{'-' * 120}")
        loop3 -= 1    
    fail()

          
def fail():
    print(f"{'-' * 120}")
    time.sleep(2)
    print(f'\nSorry {contestant_name}, looks like you\'ve lost in THE GAMESHOW....!!!\n')
    print(f"{'-' * 120}")
    game_over()
                  
def game_over():
    print(f"{'-' * 120}")
    replay = input(f'{contestant_name}, Would you like to play again? <Enter Yes/No> :\t')
    replay = replay.lower()
    if 'y' in replay or 'yes' in replay:
        tragedy_1()
    else:
        print("""
   ____                              ___                  
  / ___| __ _ _ __ ___   ___        / _ \__   _____ _ __  
 | |  _ / _` | '_ ` _ \ / _ \      | | | \ \ / / _ \ '__| 
 | |_| | (_| | | | | | |  __/      | |_| |\ V /  __/ |    
  \____|\__,_|_| |_| |_|\___|       \___/  \_/ \___|_|    
                                                              
""")
    print(f"\n{'-' * 120}")
    exit(0)

game_start()


# In[ ]:






