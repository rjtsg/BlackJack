import WriteText as WT
B = WT.B
print(B)
print(type(B))
print(B[4:6])
C = int(B[4:6])
print(C)
print(type(C))
D = C + 1
print(D)
str(D)
G = B.split()
print(G)
G[2] = str(D)
print(G)

print(type(G))
H = ' '.join(G)
print(H)
f = open('DataFile.txt','w')
f.write(H)
#f.write('A = 12')
f.close
