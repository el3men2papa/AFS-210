def pay():
    iD = input("Please enter the Employee's ID: ")
    firstName = input("Please enter the Employee's First Name: ")
    lastName = input("Please enter the Employee's Last Name: ")
    rate = float(input("Please enter the Employee's Hourly Pay Rate:"))
    hrs = float(input("How many hours did John work this week? "))

    if hrs <= 40:
        print("Please enter the Employee's ID:",iD)
        print("Please enter the Employee's First Name:",firstName)
        print("Please enter the Employee's Last Name:",lastName)
        print("Please enter the Employee's Hourly Pay Rate: $",format(rate,"8.2f"))
        print("How many hours did", firstName, "work this week?",format(hrs,"2.0f"))
        print(firstName, lastName, "paycheck amount is $",format(hrs*rate, "8.2f"))

    else:
        hours = hrs - 40
        pay = hours * (rate * 1.5)
        regularPay = 40 * rate
        print("Please enter the Employee's ID:",iD)
        print("Please enter the Employee's First Name:",firstName)
        print("Please enter the Employee's Last Name:",lastName)
        print("Please enter the Employee's Hourly Pay Rate: $",format(rate,"8.2f"))
        print("How many hours did", firstName, "work this week?",format(hrs,"2.0f"))
        print(firstName, lastName, "paycheck amount is $",format(regularPay+pay, "8.2f"))


pay()