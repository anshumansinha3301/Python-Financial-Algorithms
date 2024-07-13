def net_present_value(cash_flows, discount_rate):
    """
    Calculate Net Present Value (NPV).

    NPV is the difference between the present value of cash inflows and the present value of cash outflows over a period of time. It's used to analyze the profitability of an investment.

    :param cash_flows: List of cash flows (inflows and outflows).
    :param discount_rate: Discount rate (decimal).
    :return: NPV value.
    """
    npv = sum([cf / (1 + discount_rate) ** i for i, cf in enumerate(cash_flows)])
    return npv

# Example usage:
cash_flows = [-500, 200, 300, 400]
discount_rate = 0.1
print(net_present_value(cash_flows, discount_rate))
