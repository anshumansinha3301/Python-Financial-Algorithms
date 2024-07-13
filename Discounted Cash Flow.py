def discounted_cash_flow(cash_flows, discount_rate):
    """
    Calculate Discounted Cash Flow (DCF).

    DCF is used to estimate the value of an investment based on its expected future cash flows, discounted back to their present value.

    :param cash_flows: List of cash flows (inflows and outflows).
    :param discount_rate: Discount rate (decimal).
    :return: Present value of cash flows.
    """
    dcf = sum([cf / (1 + discount_rate) ** i for i, cf in enumerate(cash_flows)])
    return dcf

# Example usage:
cash_flows = [100, 200, 300, 400]
discount_rate = 0.1
print(discounted_cash_flow(cash_flows, discount_rate))
