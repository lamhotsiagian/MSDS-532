# Assignment 5 Problem 4
# Purpose: Determine max annual expenses post-retirement so that funds almost deplete
# Date: October 5, 2025
# Developer: Lamhot Siagian

def variableInvestor(salary, prate, vrate):
    """
    Calculate annual retirement plan value with variable growth rates.

    Parameters:
    salary (float): employee's annual salary
    prate (float): employee's investment rate as a decimal
    vrate (list of float): list of annual growth rates as decimals

    Returns:
    list: retirement plan value at the end of each year
    """
    employer_investment_rate = 0.05
    employer_match_rate = min(prate, 0.05)
    
    # First year investment without interest
    values = [salary * (prate + employer_investment_rate + employer_match_rate)]
    
    for i in range(1, len(vrate)):
        # Compound the previous year's value by (1 + vrate[i])
        end_value = values[-1] * (1 + vrate[i])
        values.append(end_value)
        
    return values

def finallyRetired(saved, vrate, expensed):
    """
    Calculate retirement account balance after annual expenses and interest.

    Parameters:
    saved (float): initial retirement savings
    vrate (list of float): list of annual return rates as decimals
    expensed (float): annual amount withdrawn from savings

    Returns:
    list: remaining balance at the end of each year
    """
    balances = []
    current_balance = saved
    
    for rate in vrate:
        # Apply interest
        current_balance *= (1 + rate)
        # Subtract annual expenses
        current_balance -= expensed
        balances.append(current_balance)
        
    return balances

def maximumExpensed(salary, prate, workRate, retiredRate, epsilon):
    """
    Use binary search to find the max annual expense post-retirement that depletes funds near zero.

    Parameters:
    salary (float): annual salary
    prate (float): saving rate as a decimal
    workRate (list of float): growth rates during working years
    retiredRate (list of float): growth rates during retirement years
    epsilon (float): maximum acceptable final balance deviation from zero

    Returns:
    float: maximum annual expense allowed
    """
    # Calculate accumulated savings during working years
    savings = variableInvestor(salary, prate, workRate)[-1]
    
    low = 0
    high = savings
    max_expense = (low + high) / 2
    
    while high - low > epsilon:
        balances = finallyRetired(savings, retiredRate, max_expense)
        final_balance = balances[-1]
        
        print(f"Trying expense: {max_expense:.2f}, Remaining balance: {final_balance:.2f}")
        
        if final_balance > 0:
            low = max_expense  # can afford more expenses
        else:
            high = max_expense  # expenses too high
        
        max_expense = (low + high) / 2
    
    return max_expense

# Example usage
salary = 50000
prate = 0.05
workRate = [0.05, 0.04, 0.06, 0.03, 0.05]
retiredRate = [0.04, 0.03, 0.05, 0.02, 0.03]
epsilon = 1  # $1 tolerance

max_expense = maximumExpensed(salary, prate, workRate, retiredRate, epsilon)
print(f"Maximum annual expense: {max_expense:.2f}")
