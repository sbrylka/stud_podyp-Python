def non_odd_than_input():
    '''returns all non odd numbers lesser than input number'''
    input_number = (int(input("Tell me a number to start having fun: ")))
    output_number = 1
    while output_number < input_number:
        print(output_number)
        output_number += 2

non_odd_than_input()