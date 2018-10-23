RFstr = ' '
line1 = ' '
line2 = ' '

def GrabRead(): #the function that reads the files
    global RFstr
    global line1
    global line2
    f = open('DataFile1.txt','r')
    B = f.read()
    RFstr = B.split()
    line1 = RFstr[0:6]
    line2 = RFstr[6:12]
    #print(RFstr)
    f.close

def GrabWrite(x): #the function that changes the file
    f = open('DataFile1.txt','w') 
    line1[5] = str(int(line1[5])+1)
    if x == 1:
        line2[1] = str(int(line2[1])+1)
    elif x == 2:
        line2[3] = str(int(line2[3])+1)
    elif x == 3:
        line2[5] = str(int(line2[5])+1)
    H = ' '.join(line1[0:6])
    HH = ' '.join(line2[0:6])
    H1 = H + '\n'
    print(H)
    print(HH)
    f.write(H1)
    f.write(HH)
    f.close

#def GrabWrite():
#   f = open('DataFile1.txt','w')
#    G[2] = str(int(G[2])+1) #adds one to the amount
#    H = ' '.join(G) #makes it one string again seperated by spaces
#    f.write(H)
 #   f.close

GrabRead() #reads the file
GrabWrite(3) #changes the file 
#GrabRead() #reads the file
