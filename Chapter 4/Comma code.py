import copy

def Stringinator(list):
    if (len(spam) != 0):
        newlist = copy.copy(list)
        newlist.insert(-1, 'and')
        string = ''
        for word in range(len(spam) + 1):
            string = string + ' ' + str(newlist[word]) 
        print(string)
    else:
        print("Please enter a list with atleast 1 value")


spam = ['apples', 'bananas', 'tofu', 'cats']


Stringinator(spam)