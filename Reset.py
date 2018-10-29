#This is the reset file for the data file
def HardReset():
    f = open('DataFile.txt', 'w')
    f.write('Times the game is played: 0 \n')
    f.write('Wins: 0 Draws: 0 Losses: 0')

HardReset()
