def sum_and_mean():
    '''Returns sum of the biggest and the lowest number and mean of numbers in list
    List is closed after input = 0'''
    number = int(input("Give me a number: "))
    numbers = []
    while number != 0:
        numbers.append(number)
        number = int(input("Give me another number: "))
    else:
        max_min_sum = max(numbers) + min(numbers)
        mean = sum(numbers)/len(numbers)
        print("Sum of the biggest and the lowest numbers = " +
              str(max_min_sum) + ".")
        print("Mean = " + str(mean))

sum_and_mean()