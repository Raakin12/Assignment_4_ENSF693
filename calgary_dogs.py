# calgary_dogs.py
# RAAKIN BHATTI
#
# A terminal-based application for computing and printing statistics based on given input.
# Detailed specifications are provided via the Assignment 4 README file.
# You must include the main listed below. You may add your own additional classes, functions, variables, etc. 
# You may import any modules from the standard Python library.
# Remember to include docstrings and comments.


import pandas as pd

def main():
    # Load data from the Excel file
    excel_file_path = 'CalgaryDogBreeds.xlsx'
    df = pd.read_excel(excel_file_path)
    
    # Set the index to be a multi-index consisting of 'Breed', 'Year', and 'Month'
    df.set_index(['Breed', 'Year', 'Month'], inplace=True)

    print("ENSF 692 Dogs of Calgary")

    # User input stage
    breed = input("Please enter a dog breed: ").strip().upper()

    # Check if the breed exists in the data
    if breed not in df.index.get_level_values('Breed').str.upper().unique():
        print("Dog breed not found in the data. Please try again.")
        return

    # Filter the data for the selected breed
    breed_data = df.loc[pd.IndexSlice[breed.upper(), :, :], :]

    # Data analysis stage
    # Get the unique years for the selected breed
    years = breed_data.index.get_level_values('Year').unique()
    # Calculate the total number of dogs for the selected breed
    total_dogs = breed_data['Total'].sum()
    # Calculate the percentage of the total number of dogs for the breed across all years
    percentage_all_years = total_dogs / df['Total'].sum() * 100
    # Count the occurrences of each month for the breed
    months = breed_data.index.get_level_values('Month').value_counts()
    # Find the maximum count of dogs in any month
    max_count = months.max()
    # Find the month(s) with the maximum count
    popular_months = months[months == max_count].index.tolist()

    # Output results
    print(f"The {breed} was found in the top breeds for years: ", ' '.join(map(str, years)))
    print(f"There have been {total_dogs} {breed} dogs registered total.")
    
    # Calculate and print the percentage of the breed in top breeds for each year
    for year in years:
        total_all_years = df.loc[pd.IndexSlice[:, year, :], 'Total'].sum()
        breed_year_total = breed_data.loc[pd.IndexSlice[breed.upper(), year, :], 'Total'].sum()
        percentage_by_year = breed_year_total / total_all_years * 100
        print(f"The {breed} was {percentage_by_year:.6f}% of top breeds in {year}.")
    
    print(f"The {breed} was {percentage_all_years:.6f}% of top breeds across all years.")
    print(f"Most popular month(s) for {breed} dogs: ", ' '.join(popular_months))

if __name__ == '__main__':
    main()
