# I did a validation to see if the user is putting the year in the range of life-expectancy.csv file (in line 19 - 24). 
# To see the range of year in the file I did an analysis in lines 66 - 72
"""
Author: Edi Carlos
Program: a program to help analyze the large amount of data from life-expectancy.csv from OurWorldInData.org

Description: program to analyze it to answer the following questions

1 What is the year and country that has the lowest life expectancy in the dataset?

2 What is the year and country that has the highest life expectancy in the dataset?

3 Allow the user to type in a year, then, find the average life expectancy for that year. Then find the country with the minimum and the one with the maximum life expectancies for that year.
"""

with open('life-expectancy.csv') as f:
    # skip the first line of the file
    next(f)

    interested_year = -1
    while interested_year < 1543 or interested_year > 2019:
        interested_year = int(input("Enter the year of interest: "))
            
        if interested_year < 1543 or interested_year > 2019:
            print("Please enter a year between 1543 and 2019\n")

    largest = float(f.readline().strip().split(',')[3])
    largest_interested = -1
    lowest = float(f.readline().strip().split(',')[3])
    lowest_interested = 300

    max_life_country = ''
    max_life_interested_country = ''
    min_life_country = ''
    min_life_interested_country = ''

    max_life_year = ''
    min_life_year = ''

    start_year = 3000
    last_year = 0

    count = 0
    average_expectancy_count = 0

    for line in f:
        # strips off leading and trailing whitespace
        clean_line = line.strip()

        # splits the string that is separated with commas ( , ) in a list
        parts = clean_line.split(',')

        life_expectancy = float(parts[3])

        # define information for the max life expectancy
        if life_expectancy > largest:
            largest = life_expectancy
            max_life_country = parts[0]
            max_life_year = parts[2]

        # define information for the min life expectancy
        if life_expectancy < lowest:
            lowest = life_expectancy
            min_life_country = parts[0]
            min_life_year = parts[2]

        # verify the first year information
        if int(parts[2]) < start_year:
            start_year = int(parts[2])

        # verify the last year information
        if int(parts[2]) > last_year:
            last_year = int(parts[2])

        # Verify if the year in the line is the intereted year to know the informations
        if int(parts[2]) == interested_year:
            
            # computing the quantity of year to get the average
            count += 1
            expectancy_in_the_line = float(parts[3])
            average_expectancy_count += expectancy_in_the_line

            # Get the max expectancy in the interested year
            if expectancy_in_the_line > largest_interested:
                largest_interested = expectancy_in_the_line
                max_life_interested_country = parts[0]

            if expectancy_in_the_line < lowest_interested:
                lowest_interested = expectancy_in_the_line
                min_life_interested_country_life_interested_country = parts[0]
    
    average_expectancy = average_expectancy_count / count
    
    print()

    print(f"The start year information in the file is: {start_year}; the last year information is {last_year}")

    print(f"The overall max life expectancy is: {largest} from {max_life_country} in {max_life_year}")
    print(f"The overall min life expectancy is: {lowest} from {min_life_country} in {min_life_year}\n")


    print(f"For the year {interested_year}")
    print(f"The average life expectancy across all countries was {average_expectancy:.2f}")
    print(f"The max life expectancy was in {max_life_interested_country} with {largest_interested}")
    print(f"The min life expectancy was in {min_life_interested_country} with {lowest_interested}")


