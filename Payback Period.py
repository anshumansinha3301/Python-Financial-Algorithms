def payback_period(initial_investment, cash_flows):
    """
    Calculate Payback Period.

    The payback period is the time it takes for an investment to generate an amount of money equal to the initial investment. It's a simple measure of investment recovery.

    :param initial_investment: Initial amount of money invested.
    :param cash_flows: List of cash inflows.
    :return: Payback period in years.
    """
    cumulative_cash_flow = 0
    for i, cash_flow in enumerate(cash_flows):
        cumulative_cash_flow += cash_flow
        if cumulative_cash_flow >= initial_investment:
            return i + 1
    return None

# Example usage:
initial_investment = 500
cash_flows = [100, 150, 200, 250]
print(payback_period(initial_investment, cash_flows))
