# Veterinary Clinic

## Setup

```
mkdir -p ~/workspace/python/exercises/vet-clinic && cd $_
django-admin startproject vetclinic
```

## Requirements

Make a Django application that helps with the operation of a Veterinarian's office.  The office needs software that keeps track of their animal patients, human owners and the primary veterinarian for each animal.

1. Pet name
2. Animal type
3. Breed (if applicable)
4. Name of their owner
5. Name of their veterinarian

### Pet List

This will list all pet names, and their owner, sorted by pet name. The name of the pet will be a hyperlink to show the pet details.

### Pet Detail

The detail view will show the following information.

1. Name
2. Species
3. Owner name
4. Veterinarian
5. Date of last visit

## Bonus Goal

1. In the pet list view, make the owner name a hyperlink that will show charges paid for each visit by that owner.
2. The charges paid view will display the owner name, and a list showing the date of each visit and the amount paid for the visit.
3. 
