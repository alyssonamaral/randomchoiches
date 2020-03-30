
import random
items=[]
i=0
print ('Press ENTER in a null item to finish the list and draw an item')
while True:
    i+=1
    item=input('Enter item %d: '%i)
    if item=='':
        break
    items.append(item)
print(f'The items in the list are:{items}')
print(f'The chosen one is: {random.choice(items)}')
perc = 100/len(items)
print ('The probability were:',perc,'%')