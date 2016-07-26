# Learning SQL Through Doing

## Setup

To get started, type the following command to check if you already have SQLite installed.

```bash
$sqlite3
```

And you should see:

```
SQLite version 3.7.15.2 2014-08-15 11:53:05
Enter ".help" for instructions
Enter SQL statements terminated with a ";"
sqlite>
```

If you do not see above result, then it means you do not have SQLite installed on your machine. Go to [SQLite Download page](http://www.sqlite.org/download.html) and download the precompiled binaries for your machine.

##### For Windows:

You will need to download sqlite-shell-win32-*.zip and sqlite-dll-win32-*.zip zipped files.

Create a folder C:\>sqlite and unzip the files in this folder which will give you sqlite3.def, sqlite3.dll and sqlite3.exe files.

Add C:\>sqlite in your PATH environment variable and finally go to the command prompt and issue `sqlite3` command.

##### For Mac:

After downloading the files, follow these steps:

```
$tar xvfz sqlite-autoconf-3071502.tar.gz
$cd sqlite-autoconf-3071502
$./configure --prefix=/usr/local
$make
$make install
```


## Instructions

1. Ensure you have the [Chinook Database](http://chinookdatabase.codeplex.com/) and [SQLite Manager Firefox add-on](https://addons.mozilla.org/en-US/firefox/addon/sqlite-manager/) installed.
1. Create a github repo for your answers. This repo will  only contain a README file in which you will write a short description of the exercise and where you can keep track of your answers.
1. If you have trouble opening the SQLite Manager once it has been installed, try opening firefox, selecting "customize" at the bottom of the hamberger menu at the top right of the page. You can then drag SQLite Manager onto the toolbar where it will be easily accessible.
1. Open SQLite Manager and select database < Connect Database and click on "Chinook_sqlite.sqlite".
1. Go ahead and click around a little bit to familarize yourself with the database
1. Optional, but helpful: draw an ERD of the Chinook database. Make sure to label primary keys, foreign keys, and indicate the type of relationship (one to one, one to many, many to many, etc) for each relationship. Use draw.io.
1. When you're ready to start the exercise, click the tab labeled "Execute SQL", type in your query, and click "Run SQL."
1. If your query is correct (i.e. it returns the data requested below) copy and paste the query to your github README. If your query doesn't return the expected results, try try again.

For each of the following exercises, provide the appropriate query. Yes, even the ones that are expressed in the form of questions. Everything from class and the [Sqlite Documentation](http://www.sqlite.org/) is fair game.

1. Provide a query showing Customers (just their full names, customer ID and country) who are not in the US.
1. Provide a query only showing the Customers from Brazil.
1. Provide a query showing the Invoices of customers who are from Brazil. The resultant table should show the customer's full name, Invoice ID, Date of the invoice and billing country.
1. Provide a query showing only the Employees who are Sales Agents.
1. Provide a query showing a unique list of billing countries from the Invoice table.
1. Provide a query that shows the invoices associated with each sales agent. The resultant table should include the Sales Agent's full name.
1. Provide a query that shows the Invoice Total, Customer name, Country and Sale Agent name for all invoices and customers.
1. How many Invoices were there in 2009 and 2011? What are the respective total sales for each of those years?(include both the answers and the queries used to find the answers)
1. Looking at the InvoiceLine table, provide a query that COUNTs the number of line items for Invoice ID 37.
1. Looking at the InvoiceLine table, provide a query that COUNTs the number of line items for each Invoice. HINT: [GROUP BY](http://www.sqlite.org/lang_select.html#resultset)
1. Provide a query that includes the track name with each invoice line item.
1. Provide a query that includes the purchased track name AND artist name with each invoice line item.
1. Provide a query that shows the # of invoices per country. HINT: [GROUP BY](http://www.sqlite.org/lang_select.html#resultset)
1. Provide a query that shows the total number of tracks in each playlist. The Playlist name should be include on the resulant table.
1. Provide a query that shows all the Tracks, but displays no IDs. The resultant table should include the Album name, Media type and Genre.
1. Provide a query that shows all Invoices but includes the # of invoice line items.
1. Provide a query that shows total sales made by each sales agent.
1. Which sales agent made the most in sales in 2009? HINT: [MAX](https://www.sqlite.org/lang_aggfunc.html#maxggunc)
1. Which sales agent made the most in sales over all?
1. Provide a query that shows the # of customers assigned to each sales agent.
1. Provide a query that shows the total sales per country. Which country's customers spent the most?
1. Provide a query that shows the most purchased track of 2013.
1. Provide a query that shows the top 5 most purchased tracks over all.
1. Provide a query that shows the top 3 best selling artists.
1. Provide a query that shows the most purchased Media Type.
