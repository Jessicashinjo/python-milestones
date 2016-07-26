# Accepting User Input

Python provides a built-in method to read user input on the command line.

## input()

```python
user_name = input("Please enter your name")
print("Well hello there {0}".format(user_name))
```

Here's a simplistic implementation of managing a bank account via a teller. In the `Teller` class, there is a `show_menu` method that shows the user a series of options, and then uses `input` to read in the number that is chosen.

Based on that option, another prompt is shown to accept a dollar value, and the appropriate action is taken on the `bank` module.

Once the action is performed, the menu is shown again so that the user can perform other actions.

```python
from bank import *

class Teller():
  """This class is the interface to a customer's bank acccount

  Methods:
    show_menu
  """

  def __init__(self):
    self.account = BankAccount()


  def show_menu(self):
    """Show teller options

    Arguments: None
    """
    print("1. Add money")
    print("2. Withdraw money")
    print("3. Show balance")
    choice = input("> ")


    if choice == "1":
      deposit = input("How much? ")
      self.account.add_money(deposit)


    if choice == "2":
      withdrawal = input("How much? ")
      self.account.withdraw_money(withdrawal)

    if choice == "3":
      print(self.account.show_balance())

    self.show_menu()




if __name__ == "__main__":
  show_menu()
```

##### bank.py

```python
import locale

class BankAccount():

  def __init__(self):
    self.balance = 0
    self.account = None

  def add_money(self, amount):
    """Add money to a bank account

    Arguments:
      amount - A numerical value by which the bank account's balance will increase
    """
    self.balance += float(amount)

  def withdraw_money(self, amount):
    """Withdraw money to a bank account

    Arguments:
      amount - A numerical value by which the bank account's balance will decrease
    """
    pass
    self.balance -= float(amount)

  def show_balance(self):
    """Show formatted balance

    Arguments:
      None
    """
    locale.setlocale( locale.LC_ALL, '' )
    return locale.currency(self.balance, grouping=True)
```

