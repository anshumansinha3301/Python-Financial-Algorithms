def future_value(principal, rate, time):
    """
    Calculate Future Value of an Investment.

    Future value is the value of an investment at a specific date in the future based on an assumed rate of growth.

    :param principal: Initial amount of money.
    :param rate: Annual interest rate (decimal).
    :param time: Number of years the money is invested or borrowed for.
    :return: Future value of the investment.
    """
    return principal * (1 + rate) ** time

# Example usage:
principal = 1000
rate = 0.05
time = 10
print(future_value(principal, rate, time))
