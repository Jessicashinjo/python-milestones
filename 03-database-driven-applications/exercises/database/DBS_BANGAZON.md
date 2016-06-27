# Bangazon! 
## The Command Line Ordering System

In this exercise, you will be allowing a user to interact with a basic product ordering database.

## Setup

1. Create a new Visual Studio console solution named *Bangazon*.

## Instructions

You will create a series of prompts that will allow the user to create various types of data in your Invoices database.

### Main Menu

```bash
*********************************************************
**  Welcome to Bangazon! Command Line Ordering System  **
*********************************************************
1. Create a customer account
2. Choose active customer
3. Create a payment option
4. Add product to shopping cart
5. Complete an order
6. See product popularity
7. Leave Bangazon!
> 
```

### Create Customer

```bash
Enter customer name
>

Enter street address
>

Enter city
>

Enter state
>

Enter postal code
>

Enter phone number
>
```

### Choose active customer

```bash
Which customer will be active?
1. John Q. Public
2. Svetlana Z. Herevazena
> 
```


### Create Payment Option

```bash
Enter payment type (e.g. AmEx, Visa, Checking)
>

Enter account number
>
```

### Add Product to Shopping Cart

> **Note:** These are examples. Add your own products to the *Product* table.

To make it easier to add multiple products, when the user selects a product to order, display the menu of products again. Make sure the last option of *Back to main menu* so the user can specify that no more products are needed.

```bash
1. Diapers
2. Case of Cracking Cola
3. Bicycle
4. AA Batteries
...
9. Done adding products 
```

### Complete an Order

##### If no products have been selected yet
```bash
Please add some products to your order first. Press any key to return to main menu.
```

##### If there are current products in an order
```bash
Your order total is $149.54. Ready to purchase
(Y/N) >

# If user entered Y
Choose a payment option
1. Amex
2. Visa
>

Your order is complete! Press any key to return to main menu.

# If user entered N, display the main menu again
```

Once the order is complete, show the main menu again, where the user can start creating another order.

##### See product popularity

```
1. AA Batteries ordered 10 times by 2 customers for total revenue of $99.90
2. Diapers ordered 5 times by 1 customers for total revenue of $64.95
3. Case of Cracking Cola ordered 4 times by 3 customers for total revenue of $27.96

-> Press any key to return to main menu
```

# References

## How to get started

You have been shown all the component parts so far in class that are needed to complete this project.

1. You can use WriteLine and ReadLine to show prompts and read user input.
1. You know how to use [`SqlConnection` and `SqlDataReader`](https://github.com/chortlehoort/nss-invoices/blob/master/Invoices/Program.cs) to query data and iterate over the returned rows.
1. You know how to insert data into a database (more references on that below).
1. You can write conditional logic with `if` or `switch`.

So start with the basics.

1. Show the main menu and read the user's choice of options with a `ReadLine`.
1. Based on what the user entered in, `WriteLine` their choice (e.g. "You chose to order a product")
1. Then create logic in each one of your conditions to accept further input (if needed).
1. Once all user input is gathered, perform the appropriate database action - a SELECT or an INSERT - and direct the user back to the main menu.

## Inserting into table with SQL

```cs
string command = @"
INSERT INTO Customer
    (FirstName, LastName, StreetAddress)
VALUES
    ('Sophia', 'Vargas', '801 Kilgore Street')
";

System.Data.SqlClient.SqlConnection sqlConnection1 = 
    new System.Data.SqlClient.SqlConnection("YOUR CONNECTION STRING");

System.Data.SqlClient.SqlCommand cmd = new System.Data.SqlClient.SqlCommand();
cmd.CommandType = System.Data.CommandType.Text;
cmd.CommandText = command;
cmd.Connection = sqlConnection1;

sqlConnection1.Open();
cmd.ExecuteNonQuery();
sqlConnection1.Close();
```

> **External reference:** [How to: Insert New Records into a Database](https://msdn.microsoft.com/en-us/library/ms233812.aspx)