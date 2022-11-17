""" 
3.1.4 Lecture & Guided Project
Date: 2022/11/16
"""


class Wallet():
    def __init__(self, initial_amount=0):
        self.balance = initial_amount

    def spend_cash(self, amount):
        if self.balance <= amount:
            print("insufficient funds")
        else:
            self.balance -= amount
    
    def add_cash(self, amount):
        self.balance += amount

    def __repr__(self):
        return f'<Wallet, Balance: ${self.balance}>'