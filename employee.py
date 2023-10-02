"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, wage, salaryType, commissionType=None):
        self.name = name
        self.wage = wage
        self.salaryType = salaryType
        self.commissionType = commissionType
        self.hours = 1
        self.commissionContracts = 0
        self.commissionRate = 0
        self.commissionBonus = 0

    def get_pay(self):
        return ((self.wage * self.hours) + (self.commissionContracts * self.commissionRate) + self.commissionBonus)

    def set_hours(self, hours):
        self.hours = hours

    def set_commission_rate(self, commissionRate):
        self.commissionRate = commissionRate

    def set_commission_contracts(self, commissionContracts):
        self.commissionContracts = commissionContracts
        
    def set_commission_bonus(self, commissionBonus):
        self.commissionBonus = commissionBonus

    def __str__(self):
        if self.salaryType == "monthly":
            if self.commissionType == "contract":
                return f"{self.name} works on a {self.salaryType} salary of {self.wage} and receives a commission for {self.commissionContracts} contract(s) at {self.commissionRate}/contract. Their total pay is {self.get_pay()}."

            elif self.commissionType == "bonus":
                return f"{self.name} works on a {self.salaryType} salary of {self.wage} and receives a bonus commission of {self.commissionBonus}.  Their total pay is {self.get_pay()}."

            return f"{self.name} works on a {self.salaryType} salary of {self.wage}. Their total pay is {self.get_pay()}."

        if self.salaryType == "hourly":
            if self.commissionType == "contract":
                return f"{self.name} works on a contract of {self.hours} hours at {self.wage}/hour and receives a commission for {self.commissionContracts} contract(s) at {self.commissionRate}/contract. Their total pay is {self.get_pay()}."
            
            if self.commissionType  == "bonus":
                return f"{self.name} works on a contract of {self.hours} hours at {self.wage}/hour and receives a bonus commission of {self.commissionBonus}.  Their total pay is {self.get_pay()}."

            
            return f"{self.name} works on a contract of {self.hours} hours at {self.wage}/hour. Their total pay is {self.get_pay()}."

        return ""


# Billie works on a monthly salary of 4000. Their total pay is 4000.
billie = Employee('Billie', 4000, "monthly")

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', 25, "hourly")
charlie.set_hours(100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', 3000, "monthly", "contract")
renee.set_commission_contracts(4)
renee.set_commission_rate(200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', 25, "hourly", "contract")
jan.set_hours(150)
jan.set_commission_contracts(3)
jan.set_commission_rate(220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', 2000, "monthly", "bonus")
robbie.set_commission_bonus(1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', 30, "hourly", "bonus")
ariel.set_hours(120)
ariel.set_commission_bonus(600)
