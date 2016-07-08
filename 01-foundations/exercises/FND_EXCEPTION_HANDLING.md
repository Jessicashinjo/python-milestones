# Basic Exception Handling

Because Python is a dynamically typed language, you need to carefully consider how to get the type of a variable and make no assumptions in your code.

Let's look at some basic code and see what harmful side-effects can happen.

```python
class BankAccount:

  def __init__(self):
    self.balance = 0

  def add_money(self, amount):
    """Add money to a bank account

    Arguments:
      amount - A numerical value by which the bank account's balance will increase
    """
    self.balance += amount

  def withdraw_money(self, amount):
    """Withdraw money to a bank account

    Arguments:
      amount - A numerical value by which the bank account's balance will decrease
    """
    self.balance -= amount
```