"""
Author: Edi Carlos
purpose: train iterating through files
"""

people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

youngest = int(people[0].split()[1])
youngest_name = ""

for person in people:
    
    print(person)
    person = person.split()
    print(person)

    person_name = person[0]
    person_age = int(person[1])

    if person_age < youngest:
        youngest = person_age
        youngest_name = person_name

print(f"\nThe youngest person is '{youngest_name}' with {youngest} years old.")




