#string = 'I am a string!'
#integer = 3
#list()
#lst = [string, integer, 1, 'the', [1,3,4,8]]
#print(lst[4][1])
# prints the 4th and then number 3 within the brackets
#print(lst[1:3])
#"the" will not be printed

#range has to be with list
#number = list(range(1,100,2))

word = '7 AM'
split_word = word.split()
print(split_word)

#numbers_2: number[::] # copies list, could also be copy()

fruit = ['apple', 'banana']
fruit.append('grape') #add to the end of the list
print(fruit)

fruit.insert(0,'orange') #puts in the front, shifts the index
print(fruit)

fruit.remove('banana') #removes banana from the list, only removing the first one it sees

.pop() #removes the last item on list (-1)
removed_fruit = fruit.pop()
    #you can find the removed item because you assigned it a variable

fruit.pop()
print('you removed {}.'.format(removed_fruit)) #to show what fruit removed

.extend(more) #add the list with whatever is in that (more) variable, concatentation same thing (+)

 .sort() # sorts by alpha and numerical
