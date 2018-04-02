time = input('Enter a time to see what meal you should eat, HH AM/PM: ')
time_script = time.split()
hour = int(time_script[0])
meridian = time_script[1]

if hour in range (7,10) and meridian == 'am':
    print('Breakfast')
elif (hour == 12  or hour in range (1,3)) and meridian == 'pm':
    print('Lunch')
elif hour in range (7,10) and meridian == 'pm':
    print('Dinner')
elif ((hour in range (10, 12) and meridian == 'pm') or ((hour == 12 or hour in range (1,5)) and meridian == 'am')):
    print('Hammer')
