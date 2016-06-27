# Alphabits

Use visual studio and C# to build a console app where the user is challenged to enter all the letters of the alphabet, one at a time, without repeating any, and without typing any non-letter characters.

## Behavior

1. After each successful input,  display the number of letters already entered.
1. After each unsuccessful input, display a helpful message explaining why the input was unsuccessful (e.g. 'not a letter', 'duplicate letter', etc.)
1. Upon completing the task (entering in all 26 letters), the user should receive some gratifying message like "Congratulations"

## Technical requirements

1. Use one Class in addition to the program file.
1. Your class should include a constructor function, an "addChar" method, and a "listLength" method.
1. Keep your user's successfully input letters as a list of characters
1. Use the String.Format method to craft your messages to users

## Bonus Requirements

1. Create a returnList Method on your class
1. Create a non-letter "Easter egg" character that will display the current list of successfully input letters (but will not add itself to the list!)
