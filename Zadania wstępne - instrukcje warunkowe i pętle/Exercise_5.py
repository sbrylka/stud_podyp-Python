def sum_of_numbers():
    '''After writing "0" returns a sum of all previous numbers'''
    number = int(input("Write a number: "))
    l = []
    while number != 0:
        l.append(number)
        number = int(input("Write another number: "))
    else:
        s = sum(l)
        print(s)

sum_of_numbers()