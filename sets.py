set1 = {2,0,-1}
set1.add(5)
print(set1)
set1.remove(0)
print(set1)
set1.discard(10)
print(set1)
#union in sets
setA = {1,10,15,12,14,19,20}
print(len(setA))
setB = {2,5,10,15,19,25}
print(len(setB))
setc  = setA.union(setB)
setD = setA | setB #other way of union
print(setc)
print(len(setc))
print(setD)

#intersection in sets
setE = setA.intersection(setB)
print(setE)
setF = setA & setB #other way of intersection
print(setF)
print(len(setF))
#for more than two sets 
S1 = {1,2,3,4,5}
S2 = {4,5,6,7,8}
S3 = {4,5,6,7,8,9}
I1 = S1 & S2 & S3 # intersection of three sets
print(I1)
I2 = S1 | S2 | S3 # union of three sets
print(I2)
#difference in sets
S5 = S1.difference(S2)
print(S5)
S6 = S2 - S1 #other way of difference
print(S6)
S7 = S1 - S2
print(S7)
#symmetric difference in sets   
S8 = S1.symmetric_difference(S2)
print(S8) 
S9 = S1 ^ S2 #other way of symmetric difference
print(S9)
#subset and superset
A = {1,2,3} 
B = {1,2,3,4,5,6}
print(A.issubset(B)) #True
print(B.issuperset(A)) #True
C = {7,8}
print(C.issubset(B)) #False
print(B.issuperset(C)) #False
