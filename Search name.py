# Program to search for a name in a list

NamesList = ['Jim', 'Bob', 'Alison', 'Jo', 'James']

ElementSought = input('Enter the name you are searching for : ')
ThisElement = 1
Found = False
for name in NamesList:
    if name == ElementSought:
        Found = True
    elif Found == False:
        ThisElement = ThisElement + 1

if Found:
   print('{0} was in element {1} in the list'.format(ElementSought, ThisElement))
else:
   print('Not found')
