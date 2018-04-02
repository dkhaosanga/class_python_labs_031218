

def to_miles(msmt, amt):
    if msmt == 'km':
        return amt * 1.60934
    elif msmt == 'ft':
        return amt / 5280
    elif msmt == 'm':
        return amt / 1609.34

    # km = 1.60934
    # ft = 5280
    # m = 1609.34

#print(to_miles('km', 2) - this is to check

def to_km(msmt, amt):
    if msmt == 'mile':
        return amt * 1.60934
    elif msmt == "ft":
        return amt * 0.0003048
    elif msmt == "m":
        return amt * 0.001


def to_ft(msmt, amt):
    if msmt == 'mile':
        return amt * 5280
    elif msmt == "km":
        return amt / 3280.84
    elif msmt == "m":
        return amt * 3.28084


def to_meters(msmt, amt):
    if msmt == 'mile':
        return amt * 1609.34
    elif msmt == "km":
        return amt * 1000
    elif msmt == "ft":
        return amt * 0.3048

def gather_info():
    from_meas = input('What measurement do you want to convert from?: ')
    amount = float(input('What is the amount you want converted?:'))
    to_meas = input('What measurement do you want this converted to?: ')
    return from_meas, to_meas, amount

print('hello message')

while True:
    frm, to, amount = gather_info()
    if to == 'km':
        result = to_km(frm, amount)
    elif to == 'mile':
        result = to_miles(frm, amount)
    elif to == 'ft':
        result = to_ft(frm, amount)
    elif to == 'm':
        result = to_meters(frm, amount)
    else:
        print("I don't understand")
        continue

    print("{} {} is {} {}".format(amount, frm, result, to))
    q = input("Would you like to convert another measurement?: ")

    if q == "no":
        print("Goodbye")
        exit()
