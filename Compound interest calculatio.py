def compound_interest(principal, rate, times_compounded, years):
    """
    Calculate Compound Interest.

    Compound interest is the interest on a loan or deposit calculated based on both the initial principal and the accumulated interest from previous periods.

    :param principal: Initial amount of money.
    :param rate: Annual interest rate (decimal).
    :param times_compounded: Number of times interest is compounded per year.
    :param years: Number of years the money is invested or borrowed for.
    :return: Total amount after interest.
    """
    amount = principal * (1 + rate / times_compounded) ** (times_compounded * years)
    return amount

# Example usage:
principal = 1000
rate = 0.05
times_compounded = 4
years = 5
print(compound_interest(principal, rate, times_compounded, years))
