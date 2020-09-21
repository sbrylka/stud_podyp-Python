def count_installment():
    '''counts a monthly installment with given number of installments and a price
    It's a first draft, I'm going to make a more complex version'''
    installments = int(input("Give me a number of installments: "))
    price = int(input("How much you want to loan?: "))
    while installments > 48 or installments < 6:
        installments = int(input("Give me a number of installments between 6-48. "))
    if installments >= 6 and installments <= 12:
        rate = 0.025
    elif installments >= 13 and installments <= 24:
        rate = 0.05
    elif installments >= 25 and installments <= 48:
        rate = 0.1
    while price > 10000 or price < 100:
         price = int(input("Give me a price between 100-10000 PLN. "))
    else:
        credit = price + price * rate
        installment = credit/installments
        print("Your installment is " + str(installment) + "PLN monthly.")
    
count_installment()