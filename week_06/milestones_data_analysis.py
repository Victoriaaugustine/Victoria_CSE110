# W06 Project Milestone Submission - Data Analysis
# Author: Victoria Goodnews Augustine

# File path (make sure the 'life-expectancy.csv' file is in the same directory)
file_path = "life-expectancy.csv"

# Initialize min and max values
lowest_life_expectancy = float("inf")
highest_life_expectancy = float("-inf")

# Open and read the file
with open(file_path) as file:
    next(file)  # Skip the header line

    for line in file:
        parts = line.strip().split(",")  # Split line into parts
        country = parts[0]
        code = parts[1]
        year = int(parts[2])
        life_expectancy = float(parts[3])

        # Check for min and max values
        if life_expectancy < lowest_life_expectancy:
            lowest_life_expectancy = life_expectancy

        if life_expectancy > highest_life_expectancy:
            highest_life_expectancy = life_expectancy

# Display results
print(f"The lowest life expectancy value in the dataset is: {lowest_life_expectancy}")
print(f"The highest life expectancy value in the dataset is: {highest_life_expectancy}")
