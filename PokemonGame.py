"""
CPS 109 - Project Pokemon Game
Problem: Currently after finishing a difficult journey the user is currently on his way home. Yet, he encounters 
unknown monster infront of him. Problem is, he is currently very injured and is only able to let his companion deal
with the monster infront of him. The only fair chance is through a game, a real one-on-one battle.
"""

import random
import time
#This is to introduce you to the game
print("Welcome, brave adventurer! Embark on a thrilling journey where challenges await at every turn. Conquer them all, claim that free journey back home risk free!")  

#This is a dictonary which will contain the main Menu
mainMenu = {}
mainMenu['1'] = "Start Game"
mainMenu['2'] = "Character Infomation"
mainMenu['3'] = "Highscore List"
mainMenu['4'] = "Exit."

#Healh Points
aiHealthPoint = 1000
userHealthPoint = 1000

#Basic Damage 
baseAttackDamage = 50

#Bonus Damage
bonusDamage = 0

#Pity System
pity= 30
aiPity = 30

#Flee Success
success = False

#Winner but exiting
winnerExit = False
    

def ClassType(randomClass):
    if randomClass == 1:
        #Returns all the fire Type 
        className = "Fire Dog"
        classType = "Fire"
        file = open("file.txt","r")
        typeImage = file.read()

        
        
        #Returns the Water Type
    elif randomClass == 2:
        className = "Fish Monster"
        classType = "Water"
        file = open("whalelord.txt","r")
        typeImage = file.read()

        
        #Returns the Earth Type
    elif randomClass == 3:
        className = "Groundy"
        classType = "Earth"
        file = open("dugtrio.txt","r")
        typeImage = file.read()

        
        #Returns the Air Type
    elif randomClass == 4:
        className = "Whoosh"
        classType = "Air"
        file = open("balloon.txt")
        typeImage = file.read()

    
    return className,classType, typeImage

#Damage Multiplyer
def multiplyerDamager(opponentClassType,playerClassType):
    #Fire Multiplyer
    if playerClassType == "Fire":
        if opponentClassType == "Water":
            return 0.5
        else:
            return 0
    #Water Multiplyer
    elif playerClassType == "Water":
        if opponentClassType == "Earth":
            return 0.5
        else:
            return 0
    #Earth Multiplyer
    elif playerClassType == "Earth":
        if opponentClassType == "Air":
            return 0.5
        else:
            return 0
    
    #Air Multiplyer
    if playerClassType == "Air":
        if opponentClassType == "Fire":
            return 0.5
        else:
            return 0
        
#Luck Multiplyer(Gives More Health)
def luckMultiplyer(health):
    luckStat = random.randint(1,100)
    if luckStat > 90:
        return 0.5
    elif luckStat > 70:
        return 0.25
    elif luckStat > 50:
        return 0.15
    else:
        return 0
    
def criticalHits(damage):
    criticalHit = random.randint(0, 10)
    if criticalHit == 5:
        return 2
    return 0

def print_hp_bar(health, max_health):
    bar_length = 20
    filled_length = int(bar_length * health / max_health)
    bar = '█' * filled_length + '-' * (bar_length - filled_length)
    print(f'[{bar}] {health}/{max_health}')


#An infinite loop which will keep trying
while True:
    #Displays the options and the actions on what they do
    print("\n**************")
    for i in mainMenu:
        print(i, mainMenu[i])
    print("**************\n")
    
    #This will make sure that any input that is placed inside will ONLY be an integer
    try:
        #Resets selection so it does not withold the value inside the previous selection
        selections = '0'
        #Asking for user input
        selections = input("\nPlease Select: ")
        
        #Starting up the game
        if selections == "1":
            
            #Confirmation to make sure their 100% want to start the game
            while True:
                if winnerExit == True:
                    break
                
                try:
                #Same as the other try, making sure anything is ONLY a string this time.
                    print("\n**************")
                    confirmation = input("\nAre you sure. Print 'Yes' if you are sure or 'No' if not:\t")
                    print("**************\n")
                    
                    #Game Finally Starts Up
                    if confirmation.lower() == 'yes':
                        aiHealthPoint = 1000
                        userHealthPoint = 1000
                        
                        #Choosing your class Type
                        classType = {}
                        classType['1'] = "Fire Type"
                        classType['2'] = "Water Type"
                        classType['3'] = "Earth Type"
                        classType['4'] = "Air Type"
                        
                        print("CHOOSE YOUR CLASS TYPE")
                        print("\n**************")
                        for entry in classType:
                            print(entry,classType[entry])
                        print("**************\n")
                        

                        #Choosing Class Types
                        while True:
                            #Make sure only integers get through
                            try:
                                choosingType = int(input("\nWhat class type would you like?\n"))
                                
                                #Choosing Fire Type
                                if choosingType == 1:
                                    userName,userClassType,userImage = ClassType(1)
                                    break
                                                                        
                                #Choosing Water Type
                                elif choosingType== 2:
                                    userName,userClassType,userImage = ClassType(2)
                                    break

                                    
                                #Choosing Earth Type
                                elif choosingType == 3:
                                   userName,userClassType,userImage= ClassType(3)
                                   break

                                #Choosing Air Type
                                elif choosingType == 4:
                                   userName,userClassType,userImage = ClassType(4)
                                   break

                                #Only class between 1-4 can be chosen
                                else:
                                    print("\nThat is not a number between 1 - 4, please try again.\n")
                                    time.sleep(1)
                                    
                            #If not a integer raises error and restart class choosing process
                            except ValueError:
                                print("\n**VALUERROR** That is not a number. Please try againn **VALUERROR**\n")
                                time.sleep(1)
                        
                        #Assigning the ai a random class
                        aiRandomClass = random.randint(1,4)
                        aiName,aiClassType,aiImage = ClassType(aiRandomClass)
                        
                        
                        #Starting Game
                        while aiHealthPoint > 0 or userHealthPoint > 0:
                            start_time = time.time()
                            
                            if success == True:
                                break
                            
                            time.sleep(2)
                            print("\n**************************")
                            
                            print(f"{aiImage}")                         
                            print(f"{aiName} Healh: {aiHealthPoint}\nOpponent Class: {aiClassType}")
                            print_hp_bar(aiHealthPoint, 1000) 
                            
                            time.sleep(2)
                            print("\n*************************************")
                            print(f"{userImage}")
                            print(f"{userName} Health: {userHealthPoint} \nUser Class: {userClassType}")
                            print_hp_bar(userHealthPoint, 1000)
                            print("\n*************************************\n")

                        
                            actionType = {}
                            actionType['1'] = "Attack"
                            actionType['2'] = "Heal"
                            actionType['3'] = "Flee"
                            
                            
                            print("CHOOSE YOUR ACTIONS ")
                            print("\n**************")
                            for entry in actionType:
                                print(entry,actionType[entry])
                            print("**************\n")
                            
                            
                            # Choosing Action Types
                            while True:
                                # Make sure only integers get through
                                try:
                                    actions = int(input("\nChoose your action (1: Attack, 2: Heal, 3: Flee):\n"))
                            
                                    # Choosing To Attack
                                    if actions == 1:
                                        #Pity Chance in case you miss or not
                                        pityChance = random.randint(0,pity)
                                        
                                        if pityChance == 0:
                                            print("You're attacked missed!")
                                            pity = 30
                                            time.sleep(1)
                                        else:
                                            pity -= 1
                                            damage = random.randint(1,baseAttackDamage)
                                            fullDamage = int(damage + (damage*multiplyerDamager(aiClassType, userClassType)) + (damage*criticalHits(damage)))
                                            aiHealthPoint -= fullDamage
                                            print(f"You've dealt {fullDamage} amount of damaged!")
                                            time.sleep(1)
                                        break
                                    # Choosing To Heal
                                    elif actions == 2:
                                        heal = random.randint(1, 50)
                                        fullHeal = int(heal + (heal*luckMultiplyer(heal)))
                                        userHealthPoint += fullHeal
                                        print(f"You've healed, {fullHeal} health")
                                        time.sleep(1)
                                        break
                            
                                    # Choosing Flee
                                    elif actions == 3:
                                        fleePercent = random.randint(0, 100)
                                        if fleePercent >= 0 and fleePercent <= 5:
                                            aiHealthPoint = 1000
                                            userHealthPoint = 100
                                            success = True
                                            print("You were able to flee your opponent.")
                                            time.sleep(1)
                                            
                                        else:
                                            print("Opponent: \"You thought you can escape ME, THE ALMIGHT\"")
                                            time.sleep(1)
                                            print("\n**Disclaimer: The Opponent is now ENRAGED and does 10 more damage**")
                                            bonusDamage += 10
                                        break
                                    
                                    else:
                                        print("\nThat is not a valid option. Please try again.\n")
                                        time.sleep(1)
                                        # If not an integer, raise error and restart action choosing process 
                                        # Only options between 1-3 can be chosen
                                except ValueError:
                                    print("\n**ValueError** That is not a number. Please try again **ValueError**\n")
                                    time.sleep(1)
                                
                            #AI deciding to Attack
                            randomAiAction = random.randint(0, 10)
    
                            if randomAiAction >= 0 and randomAiAction <= 8:
                                aiPityChance = random.randint(1,aiPity)
                                if aiPityChance == 0:
                                     print("The Opponent missed!")
                                     time.sleep(1)
                                     pity = 30
                                else:
                                    pity -= 1
                                    aiDamage = random.randint(1, baseAttackDamage)
                                    aiFullDamage = int(aiDamage + bonusDamage + (aiDamage * multiplyerDamager(userClassType, aiClassType)) + (aiDamage * criticalHits(aiDamage)))
                                    userHealthPoint -= aiFullDamage
                                    print(f"The Opponent dealt {aiFullDamage} to you!")
                                    time.sleep(1)
                                    
                            #AI deciding to Heal
                            else:
                                aiHeal = random.randint(1, 50)
                                aiFullHeal = int(aiHeal + (aiHeal * luckMultiplyer(aiHeal)))
                                aiHealthPoint += aiFullHeal
                                print(f"The Opponent healed {aiFullHeal} health!")
                                time.sleep(1)
                                
                            if aiHealthPoint <= 0 or userHealthPoint <= 0:
                                break
                            
                        #Showcasing A Draw Scenario    
                        if aiHealthPoint <= 0 and userHealthPoint <= 0:
                            print("Draw. Well done.")
                            #Play again attempt
                            while True:
                                try:
                                    playAgain = input("\nWould you like to play again?\n")
                                   
                                    if playAgain.lower() == "no":
                                        winnerExit = True
                                        break
                                    
                                    elif playAgain.lower() == "yes":
                                        break
                                    else:
                                        print("\nThat is not a valid input. Please try again\n")
                                        time.sleep(1)
                                except ValueError:
                                    print("\n**ValueError** That is not a number. Please try again **ValueError**\n")
                                    time.sleep(1)
                        #Showcasing a User Win
                        elif aiHealthPoint < 0 and userHealthPoint > 0:
                            end_time = time.time()
                            elapsed_time = end_time - start_time
                            try:
                                file = open("cps109_a1_output.txt", "r")
                            except FileNotFoundError:
                                file = open("cps109_a1_output.txt", "a+")
                                
                            #Read and obtain existing lines of code
                            file = open("cps109_a1_output.txt", "r")
                            highscoresList = file.read().splitlines()
                            
                            #To remove the first 2 lines in the beginning of highscore
                            highscoresList = [line[2:] for line in highscoresList]
                            
                            #Preparing and appending the very new entry inside the original existing code
                            output = "Highscore: " + str(userHealthPoint) + " - Time Elapsed: " + str(elapsed_time) + " - Class: " + userClassType
                            highscoresList.append(output)
                            highscoresList.sort(reverse=True)
                            
                            #Write down the new entry down on the highscore file
                            file = open("cps109_a1_output.txt", "w")
                            for i,el in enumerate(highscoresList): 
                                file.write(f"{i+1}.{el}\n")
                           
                            print("Saved Highscore!")
                            print("You Won. Well done!")
                            time.sleep(1)
                            
                            #Play Again attempt
                            while True:
                                try:
                                    playAgain = input("\nWould you like to play again?\n")
                                   
                                    if playAgain.lower() == "no":
                                        winnerExit = True
                                        break
                                    
                                    elif playAgain.lower() == "yes":
                                        break
                                    else:
                                        print("\nThat is not a valid input. Please try again\n")
                                        time.sleep(1)
                                except ValueError:
                                    print("\n**ValueError** That is not a number. Please try again **ValueError**\n")
                                    time.sleep(1)
                            
                        #Showcasing A AI Win
                        elif userHealthPoint < 0 and aiHealthPoint > 0:
                            print("You lost. Be better!")
                           
                            #Play again attempt
                            while True:
                                try:
                                    playAgain = input("\nWould you like to play again?\n")
                                   
                                    if playAgain.lower() == "no":
                                        winnerExit = True
                                        break
                                    
                                    elif playAgain.lower() == "yes":
                                        break
                                    else:
                                        print("\nThat is not a valid input. Please try again\n")
                                        time.sleep(1)
                                except ValueError:
                                    print("\n**ValueError** That is not a number. Please try again **ValueError**\n")
                                    time.sleep(1)
                            
                        
    

                    
                    #Goes back to main menu
                    elif confirmation.lower() == 'no':
                        break
                    
                    #If it not yes or no
                    else:
                        print("\nThat is not either Yes or No, please try again.\n")
                        time.sleep(1)
                        
                #If not a string raises error and restart confirmation
                except ValueError:
                    print("\n**VALUERROR** That is not a character. Please try againn **VALUERROR**\n")
                    time.sleep(1)
            
        #Explaining each character type and moves
        elif selections == '2':
            print("********************")
            print("\nThere are 4 types of classes.\n")
            print("*********************************")
            file = open("file.txt","r")
            fireDog = file.read()
            print(fireDog)
            print("\n1. Fire Dog - Good Against: Fish Monster - Worse Against: Whoosh - Normal Against: Groundy\n")
            time.sleep(2)
            print("*********************************")
            file = open("whalelord.txt","r")
            fishMonster = file.read()
            print(fishMonster)
            print("\n2. Fish Monster - Good Against: Groundy - Worse Against: Fire Dog  - Normal Against: Whoosh\n")
            time.sleep(2)
            print("*********************************")
            file = open("dugtrio.txt","r")
            groundy = file.read()
            print(groundy)
            print("\n3. Groundy - Good Against: Whoosh - Worse Against: Fish Monster - Normal Against: Fire Dog \n")
            time.sleep(2)
            print("*********************************")
            file = open("balloon.txt","r")
            whoosh = file.read()
            print(whoosh)
            print("\n4. Whoosh - Good Against: Fire Dog  - Worse Against: Groundy - Normal Against: Fish Monster\n")

            time.sleep(2)
            print("********************")
            time.sleep(10)

        
        elif selections == '3':
            #Shocasing high score file.
            highscore = open("cps109_a1_output.txt","r")
            highscoreImage = highscore.read().splitlines()
            for i in highscoreImage:
                print(i)
            time.sleep(2)

            
        
        #Stops the entire game
        elif selections == '4':
            break
        
        #Making sure that no other integers other than entry work.
        else:
            print("\n**That is not an entry. Please try again**\n")
            time.sleep(1)
            
    #Anything other an integer will raise this error
    except ValueError:
        print("\n**VALUERROR** Please input a number between 1-3 **ValueError**\n")
        time.sleep(1)
    
