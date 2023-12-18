# This is not part of ATB
# This is some crunching to help me understand a mathematical issue I have


# Basically I am investing the expressions a^b and b^a, so far when both are real numbers greater than 1 and a<b. I am trying to find a 
# method which will help me do this very easily. 

# First I would want to confirm if 3^b is indeed greater than b^3 for all real values greater than 3
work=[]

for a in range(80):
    b=a+0.1
    works = True 
    testAmount=50
    for i in range(testAmount):
        difference = a**b - b**a
        if difference <= 0:
            works = False
        b+=0.1
        if i==testAmount-1:
            print(a)
        if works and i==testAmount-1:
            work.append(a)

print(work)

#The results are that work is a set that contains every positive integer greater than or equal to three. 3 is the lowest integer in which a^b idea 
#holds, so why does it not hold for 2?. Where is the point where it stops holding? If it holds for 4 or 5 will the 
# reverse also hold will it mean that it makes finding inequalities extremely easy?