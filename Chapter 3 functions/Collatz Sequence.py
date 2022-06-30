import sys,time

print("Enter any Integer and watch it boom to 1")

def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(number * 3 + 1)
        return number * 3 + 1
try:
    num= int(input())


    while True:
        if num != 1:
            num = collatz(num)
            time.sleep(0.1)
        else:
             sys.exit()
except ValueError:
    print('Enter an Integer please')