#Patient Information

## Requirements

Create a clinic application and display in the browser the view a doctor would see when he/she walks into the exam room with a specific patient in them.  This should include the patient's name, date of birth, a list of their medications and a list of their ailments.  

## Setup

1. Open Visual Studio and create a new empty MVC project.
    * In Visual Studio start page click on New Project (file -> new project if not on start page)
    * Select ASP.NET Web Application and give it a name
    * Click OK
    * Under ASP.NET 4.6 Templates select Empty MVC
    * Under "Add folders and Core References for:" check the MVC box
    * Click OK
2.  Make a new SQL database (see the [entity framework resource file](https://github.com/nashville-software-school/csharp-dotnet-milestones/blob/LSDatabases/3-database-driven-applications/exercises/database/DBS_V8_LINQ%2BENTITYFRAMEWORK.md) for instructions).

## Instructions

1. Make a database of three tables, Patient Profile, Medication and Ailment
2. Give properties to each of these tables including a primary key and any properties necessary for displaying the required data.
3. Populate the tables with example data.
4. Write the Models for each table and a corresponding controller for handling the data.
5. Make View Models and Views to display the data to the brower.  

## Bonus Criteria
1. Add a bill view for each patient that gives an itemized list of their medications and procudures.
2. Add a style sheet and use CSS to display the data.

