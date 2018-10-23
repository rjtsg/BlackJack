#Here the blackjack game will be programmed

import sys
import random
import Cards as C
i = True

#Start The programm
while i == True:
    print('Are you ready to play Black? (y/n)')
    x = input()
    if x == 'y':
        #deal card
        #print('Lets play')
        break
    elif x == 'n':
        sys.exit() #stop the script
    else:
        print('Only answer with y or n') #and go back to the Top
    
    
print('Lets deal the cards')    
#the probel is that each card can only be picked once,
#this means that the card needs to be removed from the ones the dealer is
#allowed to pick

#lets first pick a type of card and deal you a number
DealCards = True
n = True
PlayerPoints = 0

while n == True:
    if DealCards == True:
        for PlayerGetCards in range(2): #Dealing the player its initial 2 cards
            #print(GetCards)
            TypeName = random.choice(C.TypeNames)
            Which = random.choice(C.CardDict[TypeName])

            print(str(Which) + ' of ' + TypeName)

            New = C.CardDict[TypeName] #values that needs to be modified
            Index = New.index(Which) #get the index of the drawn card
            del New[Index] #delete that drawn card from the row
            C.CardDict[TypeName] = New #replace the values without the drawn card
            print(C.CardDict)
            PlayerPoints = PlayerPoints + Which #Keep track of the points of the player
        print(PlayerPoints)
        for DealerGetCards in range(2):
            DealerType = random.choice(C.TypeNames)
            DealerWhich = random.choice(C.CardDict[TypeName])
            print(str(Which) + ' of ' + TypeName)
            New = C.CardDict[TypeName] #values that needs to be modified
            Index = New.index(Which) #get the index of the drawn card
            del New[Index] #delete that drawn card from the row
            C.CardDict[TypeName] = New #replace the values without the drawn card
            DealerPoints = DealerPoints + Which #Keep track of the points of the player
        print(DealerPoints)
        DealCards = False #To stop the dealing of the initial two cards
    else:
        if PlayerPoints == 21:
            print('Congratulations you have gotten Blackjack')
            break #for now close the programm after a game
        elif PlayerPoints > 21:
            print('You are "Dead", you have lost')
            break 
        elif PlayerPoints < 21:
            print('you can take a hit or stay where you are')
            i = True
            while i == True:
                print('Do you want to take a hit (h) or stay(s)')
                x = input()
                if x == 'h':
                    #deal card
                    print('hit')
                    TypeName = random.choice(C.TypeNames) #picks a card class
                    Which = random.choice(C.CardDict[TypeName]) #picks a card from the class
                    print(str(Which) + ' of ' + TypeName) #prints what card there was picked
                    New = C.CardDict[TypeName] #values that needs to be modified
                    Index = New.index(Which) #get the index of the drawn card
                    del New[Index] #delete that drawn card from the row
                    C.CardDict[TypeName] = New #replace the values without the drawn card
                    #print(GameCards)
                    PlayerPoints = PlayerPoints + Which #Keep track of the points of the player
                    print(PlayerPoints)
                    i = False
                    continue
                elif x == 's':
                    print('You want to stay, you win if your cards are higher than the dealer his cards')
                    #DealerPoints = 19      
                    if PlayerPoints > DealerPoints:
                        print('Player Wins')
                        break
                    elif PlayerPoints < DealerPoints:
                        print('Dealer Wins')
                        break
                    else:
                        print('The game ends in a draw')
                        break
                else:
                    print('Only answer with h or s') #and go back to the Top

        
    
print('Thanks for playing')
