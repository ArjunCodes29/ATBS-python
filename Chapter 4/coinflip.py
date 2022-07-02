import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    listOfCoins = []
    for i in range(100):
        if (random.randint(0,1)==0):
            listOfCoins.append(1)
        else:
            listOfCoins.append(0)
    # Code that checks if there is a streak of 6 heads or tails in a row.
    for i in range(len(listOfCoins)-6):
        if (listOfCoins[i]==0 and listOfCoins[i + 1]==0 and listOfCoins[i + 2]==0 and listOfCoins[i + 3]==0 and listOfCoins[i + 4]==0 and listOfCoins[i + 5]==0 and listOfCoins[i + 6]==0):
            numberOfStreaks += 1
            break
        elif (listOfCoins[i]==1 and listOfCoins[i + 1]==1 and listOfCoins[i + 2]==1 and listOfCoins[i + 3]==1 and listOfCoins[i + 4]==1 and listOfCoins[i + 5]==1 and listOfCoins[i + 6]==1):
            numberOfStreaks += 1
            break
print('Chance of streak: ' + str((numberOfStreaks / 10000) *100) + '%')