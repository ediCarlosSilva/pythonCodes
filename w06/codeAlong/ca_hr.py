with open ('hr_system.txt') as f:
    # skips the first file line
    next(f)

    for line in f:
        # Strips off leading and trailing whitespace
        clean_line = line.strip()
        
        # splits the string into a list
        parts = clean_line.split()
        name = parts[0]
        id_number = parts[1]
        title = parts[2]
        salary = float(parts[3])

        # print(f"{name} (ID: {id_number}), {title} - ${salary:.2f}")

        # Calculate the paycheck amount
        paycheck_amount = salary/24

        # Adds a bonus
        if title.lower() == "engineer":
            paycheck_amount += 1000

        print(f"{name} (ID: {id_number}), {title} - ${paycheck_amount:.2f}")
        print()

#  Alexia (ID: 1913), Engineer - $84000.00
# Herman (ID: 4266), Manager - $106000.00
# Jay (ID: 5849), Engineer - $93000.00
# Ahmad (ID: 1326), Tester - $85000.00n