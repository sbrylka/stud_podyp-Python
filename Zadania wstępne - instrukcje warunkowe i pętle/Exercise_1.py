def bmi_calc():
    waga = int(input("podaj wagę: "))
    wzrost = float(input("podaj wzrost: "))

    if wzrost > 3:
        wzrost /= 100
    bmi = waga/(wzrost*wzrost)
    if bmi > 24.9:
        print("\nTwoja waga jest za wysoka.")
    elif bmi < 18.5:
        print("\nTwoja waga jest za niska.")
    else:
        print("\nTwoja waga jest prawidłowa.")
        
bmi_calc()