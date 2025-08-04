# W06 Project: Data Analysis
# Author: Victoria Goodnews Augustine
# Creative Extension: User can also type a country name to see its min, max, and average life expectancy across all years.

file_path = "life-expectancy.csv"

# Initialize overall min and max trackers
overall_min = float("inf")
overall_min_country = ""
overall_min_year = 0

overall_max = float("-inf")
overall_max_country = ""
overall_max_year = 0

# Load data into a list
data = []
with open(file_path) as file:
    next(file)  # skip header
    for line in file:
        parts = line.strip().split(",")
        country = parts[0]
        code = parts[1]
        year = int(parts[2])
        life_expectancy = float(parts[3])
        data.append((country, code, year, life_expectancy))

        # Check for overall min and max
        if life_expectancy < overall_min:
            overall_min = life_expectancy
            overall_min_country = country
            overall_min_year = year

        if life_expectancy > overall_max:
            overall_max = life_expectancy
            overall_max_country = country
            overall_max_year = year

# Display overall results
print(f"\nThe overall max life expectancy is: {overall_max} from {overall_max_country} in {overall_max_year}")
print(f"The overall min life expectancy is: {overall_min} from {overall_min_country} in {overall_min_year}\n")

# Prompt for user input year
year_of_interest = int(input("Enter the year of interest: "))

# Filter data for the chosen year
year_data = [entry for entry in data if entry[2] == year_of_interest]

if year_data:
    year_total = 0
    year_min = float("inf")
    year_max = float("-inf")
    year_min_country = ""
    year_max_country = ""

    for entry in year_data:
        country, _, _, life_expectancy = entry
        year_total += life_expectancy

        if life_expectancy < year_min:
            year_min = life_expectancy
            year_min_country = country

        if life_expectancy > year_max:
            year_max = life_expectancy
            year_max_country = country

    year_average = year_total / len(year_data)

    print(f"\nFor the year {year_of_interest}:")
    print(f"The average life expectancy across all countries was {year_average:.2f}")
    print(f"The max life expectancy was in {year_max_country} with {year_max}")
    print(f"The min life expectancy was in {year_min_country} with {year_min}")
else:
    print(f"No data found for the year {year_of_interest}.")

# Creative Extension: User can also type a country to analyze
country_input = input("\nWould you like to analyze a specific country? (Type country name or press Enter to skip): ").strip()

if country_input:
    country_data = [entry for entry in data if entry[0].lower() == country_input.lower()]

    if country_data:
        total = 0
        min_life = float("inf")
        max_life = float("-inf")
        min_year = 0
        max_year = 0

        for entry in country_data:
            _, _, year, life_expectancy = entry
            total += life_expectancy

            if life_expectancy < min_life:
                min_life = life_expectancy
                min_year = year

            if life_expectancy > max_life:
                max_life = life_expectancy
                max_year = year

        avg_life = total / len(country_data)

        print(f"\nAnalysis for {country_input.title()}:")
        print(f"Average life expectancy: {avg_life:.2f}")
        print(f"Minimum life expectancy: {min_life} in {min_year}")
        print(f"Maximum life expectancy: {max_life} in {max_year}")
    else:
        print(f"No data found for {country_input}.")
