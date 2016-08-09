# Patient Information

## Setup

```
mkdir -p ~/workspace/python/exercises/patients && cd $_
django-admin startproject doctorclinic
```

## Requirements

Create a Django clinic application and display in the browser the view a doctor would see when he/she walks into the exam room with a specific patient in them. Define three models for your application - Patient, Medication and Ailment - with appropriate properties (_see below_).

### Patient List

This view will simply list all patients sorted by last name. Each patient name will be a hyperlink to the patient overview view.

### Patient Overview

This view will display the following information:

1. Full name.
2. Age.
3. Date of last visit.
4. List of known ailments. Each ailment will be a hyperlink to the ailment detail view.
5. List of known medications. Each ailment will be a hyperlink to the ailment detail view.

### Patient Ailment

This view will show the ailment and the date that it was diagnosed.

### Patient Medications

This view will show the medication and the date that it was prescribed.

This should include the patient's name, date of birth, a list of their medications and a list of their ailments.  

## Bonus Criteria

1. Add a bill view for each patient that gives an itemized list of their medications and procudures.
2. Add a style sheet and use CSS to display the data.

