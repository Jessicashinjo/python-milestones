# Veterinary Clinic

## Setup

```
mkdir -p ~/workspace/python/exercises/vet-clinic && cd $_
sqlite3 vetclinic.db
```

## Instructions

This exercise mocks the operations of a Veterinarian's office.  The office needs software that keeps track of their animal patients, human owners and the primary veterinarian for each animal. Make a Django application that responds with a web page containing a list of pets with the following properties:

1. Pet name
2. Animal type
3. Breed (if applicable)
4. Name of their owner 
5. Name of their veterinarian

## Requirements

1. Each pet should include their name (i.e. Fido), species (cat, dog, etc.), breed (if applicable), human owner and veterinarian.
2. Populate the tables with example data, give each veternatian several patients and at least 3 humans more than one pet.
3. Make at least 3 tables.
4. Use SQL to join the 3 tables to retrieve the data for the list.

## Bonus Criteria

1. Make a patient profile view that gives the name, owner and veterinarian of a single animal
2. Make a fourth table that lists charges for vet services. Populate this with sample data that tracks the vet, the owner, and the price for the service.  Then use SQL to make an invoice for the pet owner.

