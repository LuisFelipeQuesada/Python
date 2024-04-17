# 5. Class Variables: Define a class BankAccount with a class variable bank_name and instance variables account_holder_name,
# balance. Initialize the class variables in the constructor and add methods like deposit() and withdraw() to perform transactions.
# Create two instances of the BankAccount class and verify that the class variable is shared

class BankAccount:

    __bank_name = ""

    def __init__(self, bank_name, holder_name, balance):
        self.__bank_name = bank_name
        self. account_holder_name = holder_name
        self.balance = balance

    def get_bank_name(self):
        return self.__bank_name

b1 = BankAccount("Bank of America", "Marcus Aurelius", "500.000")
b2 = BankAccount("City", "Marcus Aurelius", "500.000")
    
print(b1.get_bank_name())
print(b2.get_bank_name())