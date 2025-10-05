# Assignment 5 Problem 1
# Purpose: To calculate retirement plan value annually using fixed growth rate and fixed contributions
# Date: October 5, 2025
# Developer: Lamhot Siagian

def fixedInvestor(salary, prate, frate, years):
    """
    Calculate annual retirement plan value with fixed growth and contributions.

    Parameters:
    salary (float): annual salary of the employee
    prate (float): employee's investment rate as a decimal (e.g., 0.05 for 5%)
    frate (float): fixed annual growth rate as a decimal (e.g., 0.05 for 5%)
    years (int): number of years to calculate

    Returns:
    list: retirement plan value at the end of each year
    """
    # Initial investment calculations
    employer_investment_rate = 0.05
    employer_match_rate = min(prate, 0.05)
    
    # Calculate the first year's investment without interest
    first_year_value = salary * (prate + employer_investment_rate + employer_match_rate)
    
    values = [first_year_value]
    
    for year in range(1, years):
        # Compound the previous year's value by (1 + frate)
        end_value = values[-1] * (1 + frate)
        values.append(end_value)
        
    return values

# Example usage
salary = 50000
prate = 0.05
frate = 0.05
years = 5

retirement_values = fixedInvestor(salary, prate, frate, years)
print(retirement_values)
