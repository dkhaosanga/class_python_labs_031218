# Integers: Integers are whole numbers,
# Floating numbers are numbers with decimals.  Both
# positive and negative numbers

#Arithmetic operators:
# addition +, integers and floats can be mixed and matched
# subtraction -, integers and floats mixed and matched
# multiplication *, mixed and matched, you can mutiply variable with integers
# division /, will always print as a floats
# floor division //, rounds down, takes off everything after the decimal
# modulus operators %, gives you the remainder, helpful to determine even or odds print % 2
# print(20 % 4)
# print(40 % 9)

# Exponents **, print(20 ** 3), cubed

# +=, -=, *= so you don't have to reassign a variable
# number = 10
# number += 5
# print(number) will equal 15

#lab 3 - hammer
# When asking for time with hour and am or pm ask with this: (HH:AM/PM)
# meridan is the AM/PM
time = input("what time is it? ")
time_split = time.split(':') #automatically if you put just () it will be a space
hour = int(time_split[0])
meridian = (time_split[1]) #.lower(), you can put in after input

if hour in range (7,10):
    if meridian == 'am':
        print("it's breakfast")
    else:
        print("it's dinner") #taking hours and then if theres any other meridian it will print dinner
elif hour in range (10,12) and meridian == "pm" or (hour == 12 or hour in range (1,5) and meridian == "am"):
    
