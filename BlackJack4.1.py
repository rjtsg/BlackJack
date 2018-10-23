#Here the blackjack game will be programmed

import sys
import random
import Cards as C
i = True


    
    
#Make here the initiations    

DealCards = True #This starts the came to let the dealer and player get their cards
n = True
PlayerPoints = 0 #Define the points of the player
Cards = C.CardDict #Load cards in so you can change the deck
DealerPoints = 0 #Define the points of the Dealer
DealerCards = [] #make a list of all the cards the dealer has
DealersTurn = True #initiate dealers turn
FirstGame = True #to know what text to show the player
RFstr = '' #this is the global read file string
line1 = '' #this is the first line in the DataFile
line2 = '' #second line of the DataFile

#Set here the functions
def GrabRead(): #the function that reads the files
    global RFstr
    global line1
    global line2
    f = open('DataFile.txt','r')
    B = f.read()
    RFstr = B.split()
    line1 = RFstr[0:6]
    line2 = RFstr[6:12]
    f.close

def GrabWrite(): #the function that changes the file
    f = open('DataFile.txt','w')
    line1[5] = str(int(line1[5])+1)
    L1 = ' '.join(line1[0:6])
    L2 = ' '.join(line2[0:6])
    L1 = L1 + '\n'
    f.write(L1)
    f.write(L2)
    f.close

def GrabWins():
    f = open('DataFile.txt','w')
    L1 = ' '.join(line1[0:6])
    L1 = L1 + '\n'
    line2[5] = str(int(line2[5]) + 1)
    L2 = ' '.join(line2[0:6])
    f.write(L1)
    f.write(L2)
    f.close

def BlackJack():
    #this section is needed to make the global variables
    global DealCards
    global i
    global n
    global PlayerPoints
    global Cards
    global DealerPoints
    global DealerCards
    global DealersTurn
    while n == True:
        if DealCards == True:
            for PlayerGetCards in range(2): #Dealing the player its initial 2 cards
                #print(GetCards)
                TypeName = random.choice(C.TypeNames)
                Which = random.choice(Cards[TypeName])

                print('You get a ' + str(Which) + ' of ' + TypeName)

                New = Cards[TypeName] #values that needs to be modified
                Index = New.index(Which) #get the index of the drawn card
                del New[Index] #delete that drawn card from the row
                Cards[TypeName] = New #replace the values without the drawn card
                PlayerPoints = PlayerPoints + Which #Keep track of the points of the player
            #print(PlayerPoints)
            for DealerGetCards in range(2): #Dealing the dealers initial 2 cards
                DealerTypeName = random.choice(C.TypeNames) 
                DealerWhich = random.choice(Cards[DealerTypeName])
                #print(str(DealerWhich) + ' of ' + DealerTypeName)
                New = Cards[DealerTypeName] #values that needs to be modified
                Index = New.index(DealerWhich) #get the index of the drawn card
                del New[Index] #delete that drawn card from the row
                Cards[DealerTypeName] = New #replace the values without the drawn card
                DealerPoints = DealerPoints + DealerWhich #Keep track of the points of the dealer
                DealerCards.append(DealerTypeName) #puts in the type of the card
                DealerCards.append(DealerWhich) #puts in the value of the card
            #print(DealerPoints)
            #print(DealerCards)
            print('The Dealer has a ' + str(DealerCards[1]) + ' of ' + DealerCards[0])
            
            DealCards = False #To stop the dealing of the initial two cards
        else:
            if PlayerPoints == 21:
                print('Congratulations you have gotten Blackjack')
                GrabWins()
                return()
            elif PlayerPoints > 21:
                print('You are "Dead", you have lost')
                return() 
            elif PlayerPoints < 21:
                #print('you can take a hit or stay where you are')
                o = True
                while o == True:
                    print('Do you want to take a hit (h) or stay(s)')
                    x = input()
                    if x == 'h':
                        #deal card
                        print('hit')
                        TypeName = random.choice(C.TypeNames) #picks a card class
                        Which = random.choice(Cards[TypeName]) #picks a card from the class
                        print(str(Which) + ' of ' + TypeName) #prints what card there was picked
                        New = Cards[TypeName] #values that needs to be modified
                        Index = New.index(Which) #get the index of the drawn card
                        del New[Index] #delete that drawn card from the row
                        Cards[TypeName] = New #replace the values without the drawn card
                        #print(GameCards)
                        PlayerPoints = PlayerPoints + Which #Keep track of the points of the player
                        print(PlayerPoints)
                        o = False
                        #continue
                    elif x == 's':
                        print('You stay, you win if your cards are higher than the dealer his cards')
                        print('The dealers second card is a ' + str(DealerCards[3]) + ' of ' + DealerCards[2])
                        #DealerPoints = 19
                        while DealersTurn == True: #let the dealer pick his new cards
                            if DealerPoints > PlayerPoints: #if the dealer has more points after the card reveal stay
                                print('The dealer stays')
                                DealersTurn = False #the dealer does not pick another card
                            elif DealerPoints < PlayerPoints:
                                print('The dealer draws another cards')
                                DealerTypeName = random.choice(C.TypeNames) 
                                DealerWhich = random.choice(Cards[DealerTypeName])
                                New = Cards[DealerTypeName] #values that needs to be modified
                                Index = New.index(DealerWhich) #get the index of the drawn card
                                del New[Index] #delete that drawn card from the row
                                Cards[DealerTypeName] = New #replace the values without the drawn card
                                DealerPoints = DealerPoints + DealerWhich #update the dealers points
                                print('The dealer gets a ' + str(DealerWhich) + ' of ' + DealerTypeName) #show what card the dealer drawed
                                #print(DealerPoints) # to check for errors
                                if DealerPoints < 21: #go through the loop again if dealer points are lower than 21
                                    continue
                                if DealerPoints >= 21: 
                                    break #break the loop because the dealer has balckjack or is dead
                            elif DealerPoints == PlayerPoints:
                                break #break while loop
                            
                        if DealerPoints > 21:
                            print('The dealer is dead, the player wins')
                            GrabWins()
                            return()
                        elif DealerPoints == 21:
                            print('The dealer has gotten Blackjack, the player loses')
                            return()   
                        elif PlayerPoints > DealerPoints:
                            print('Player Wins')
                            GrabWins()
                            return()
                            
                        elif PlayerPoints < DealerPoints:
                            print('Dealer Wins')
                            return()
                        else:
                            print('The game ends in a draw')
                            return()
                    else:
                        print('Only answer with h or s') #and go back to the Top

#Start The programm
while i == True:
    if FirstGame == True:
        print('Are you ready to play Blackjack? (y/n)')
        x = input()
        if x == 'y':
            #deal card
            #print('Lets play')
            #break
            FirstGame = False
            GrabRead()
            GrabWrite()
            BlackJack()
        elif x == 'n':
            sys.exit() #stop the script
        else:
            print('Only answer with y or n') #and go back to the Top
    elif FirstGame == False:
        DealCards = True #To make sure the game deals the cards again
        print('Do you want to play another round (y/n)')
        x = input()
        if x == 'y':
            PlayerPoints = 0 #reset player points
            DealerPoints = 0 #reset player points
            Cards = C.CardDict #reset Deck
            DealersTurn = True #gives dealer his turn back
            DealerCards = [] #reset the dealers cards
            GrabRead()
            GrabWrite()
            BlackJack()
        elif x == 'n':
            sys.exit() #stop the script
        else:
            print('Only answer with y or n') #and go back to the Top
        
    
print('Thanks for playing')
