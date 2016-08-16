# Writing SQL with Python

Python has a [built-in package](https://docs.python.org/3.3/library/sqlite3.html) for making a connection to a SQLite database. It's called `sqlite3`. Here's a basic example of how to connect to a database and execute SQL statements.

```py
import sys
import sqlite3
from datetime import datetime
from time import time

class Amazon:
  '''A simplified class to buy stock in Amazon'''


  def __init__(self):
    pass


  def buy_amazon(self, quantity, purchase_price):
    '''Allows a user to purchase Amazon stock

    Method arguments
    ----------------
      quantity -- (integer) The number of stocks to purchase
      purchase_price -- (real) The price at which the stocks were purchased
    '''
    with sqlite3.connect('example.db') as conn:
      c = conn.cursor()

      try:
        c.execute("""create table stocks
          (date text, trans text, symbol text, qty real, price real)""")
      except sqlite3.OperationalError:
        pass

      timestamp = time()
      date = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
      trans = "BUY"
      symbol = "AMZN"
      qty = 100
      price = 95.51

      c.execute("insert into stocks values (?, ?, ?, ?, ?)",
                    (date, trans, symbol, quantity, purchase_price))

      conn.commit()

  def query_all_amazon(self):
    '''Query and print all of the transactions for purchased Amazon stocks

    Method arguments
    ----------------
      n/a
    '''

    with sqlite3.connect('example.db') as conn:
      c = conn.cursor()

      c.execute("select * from stocks where trans=? and symbol=?", ("BUY", "AMZN"))
      conn.commit()
      print(c.fetchall())

  def query_latest_amazon(self):
    '''Query and print last transaction

    Method arguments
    ----------------
      n/a
    '''

    with sqlite3.connect('example.db') as conn:
      c = conn.cursor()

      c.execute("select * from stocks where trans=? and symbol=? order by date desc", ("BUY", "AMZN"))
      conn.commit()
      print(c.fetchone())


  def clear_database(self):
    '''Deletes all transactions from the database

    Method arguments
    ----------------
      n/a
    '''
    with sqlite3.connect('example.db') as conn:
      c = conn.cursor()

      c.execute("delete from stocks")
      conn.commit()



if __name__ == "__main__":
  amz = Amazon()
  # amz.clear_database()
  # amz.buy_amazon(sys.argv[1], sys.argv[2])
  amz.query_latest_amazon()
  # amz.query_all_amazon()
```

## Helpers to Focus On

* [execute](https://docs.python.org/3.3/library/sqlite3.html#sqlite3.Cursor.execute) will execute a single SQL statement
* [executescript](https://docs.python.org/3.3/library/sqlite3.html#sqlite3.Cursor.executescript) allows you to execute multiple statements at the same time
* [fetchone](https://docs.python.org/3.3/library/sqlite3.html#sqlite3.Cursor.fetchone) retrieves the next row, represented as a tuple, in a resultset. Helpful if you know that your SQL should only return one row.
* [fetchall](https://docs.python.org/3.3/library/sqlite3.html#sqlite3.Cursor.fetchall) will produce a list containing tuples that represent each row in the resultset of your query.