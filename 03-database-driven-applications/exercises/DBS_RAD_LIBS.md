# Rad Libs

## Setup

```
mkdir -p ~/workspace/python/exercises/radlibs && cd $_
```

## Instructions

A recreation of the classic Mad Libs game as a Django web app.  Users are prompted to enter a series of words via a form which are then used to populate a short story.  The incongruity between randomly selected words and the narritive flow of the story generally leads to a funny outcome.  Users should have to enter _at least_ one of each of the following parts of speech:

1. Noun
2. Verb
3. Adjective
4. Adverb
5. Interjection

## Requirements

1. All words to complete the story should be entered at once via a single form
2. Each of the parts of speech should be stored in their own table
3. After completing the Rad Lib with their own entries, the user should be able to:
  - click a button/link to repeat the Rad Lib with different entries
  - click a button/link to populate the Rad Lib with random entries from the database

## Bonus Criteria

1. On the entry page, provide users a choice of several Rad Libs stories to populate listed by story title.
2. Adust the form to contain the correct number of fields for fillable areas in the Rad Lib.
