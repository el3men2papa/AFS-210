

id = input("Please enter the Employee's ID: ")
firstName = input("Please enter the Employee's First Name: ")
lastName = input("Please enter the Employee's Last Name: ")
rate = float(input("Please enter the Employee's Hourly Pay Rate:"))
hrs = float(input("How many hours did work this week? "))

class Employee:
    def __init__(self,id,fname,lname,hourlypay):
        self.iD = id
        self.firstName = fname
        self.lastName = lname
        self.rate = hourlypay
        
    def pay(self,hrs): 
        
        if hrs <= 40:
            return format(hrs*rate, "8.2f")
        else:
          hours = hrs - 40
          pay = hours * (rate * 1.5)
          regularPay = 40 * rate 
        return format(regularPay+pay, "8.2f")


emp = Employee(id, firstName, lastName, rate)

print("Please enter the Employee's ID:",emp.iD)
print("Please enter the Employee's First Name:",emp.firstName)
print("Please enter the Employee's Last Name:",emp.lastName)
print("Please enter the Employee's Hourly Pay Rate: $",format(emp.rate,"8.2f"))
print("How many hours did", emp.firstName, "work this week?",format(hrs,"2.0f"))
print(emp.firstName, emp.lastName, "paycheck amount is $",emp.pay(hrs))

