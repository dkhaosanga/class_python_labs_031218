
def validation():
    number = input('What is the credit card number without dashes?: ')
    cc_number = list(number)
    print(cc_number)

    remove_last_digit = cc_number.pop()
    print(cc_number)
    # print(remove_last_digit)

    # return (cc_number[::-1])
    print(cc_number[::-1])

    # for i in range(len(cc_number)):
    #     if i % 2 == 0:
    #         cc_number[i] = cc_number[i]*2
    # print(cc_number)






validation()
