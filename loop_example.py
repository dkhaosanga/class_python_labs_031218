fruit = ['apple', 'banana', 'orange', 'grape']

for item in fruit:
#[-1,1] for just item in list.. item stands for "thing", apples, banana
    print(item)
    #print(item.upper())

#item += item

for i in range(101): #prints 0-100
    print(i)

#when you want the lenth of fruit, it will count each
#for i in range(len(fruit)):
#print(fruit[i]) # gives you the index of i, printing out each thing, giving each thing a number

#WHILE LOOPS, need a boliun (true or false) after them use break or exit() to stop, exit will not pring out anything after
i = 0
while True:
    print(i)
    i += 1
    break

#this is to prompt an exit
 #while i < 1000:
    #i += 1
    #print(i)

#to print even number in list
for i range (101):
    if i % 2 == 1: #module
        continue #stop current loop and starts at the top
    print(i) #won't occur since there is a continue
