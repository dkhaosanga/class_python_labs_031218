greeting = "hello, {}!"
name = input("What is your name?: ")
total_greeting = greeting.format(name.captitalize())
print(total_greeting)
print(total_greeting.count('l'))
# .index('y') gives you where the location of where y is [3]
print(total_greeting.index('y'))
