import sys,time

#def printer(x):
    #print( x * ' ' + '********')


#while True:
    #for i in range(4,0,-1):
       # printer(i)
        #time.sleep(0.1)
    #for i in range(1,5,1):
        #printer(i)
        #time.sleep(0.1)

#The above was my attempt based on the output i saw

indentNumber = 0
indentIncreasing = True

try:
    while True:
        print(' ' * indentNumber + '********' )
        time.sleep(0.1)

        if indentIncreasing:
            indentNumber = 1 + indentNumber
            if indentIncreasing == 10:
                indentIncreasing = False
        
        else:
            indentNumber = indentNumber - 1
            if indentNumber==0:
                indentIncreasing = True

except KeyboardInterrupt:
    sys.exit()




#this doesnt seem to be working for some reason instead of changing the amount of indent its chanigng the space between each row of asteriks