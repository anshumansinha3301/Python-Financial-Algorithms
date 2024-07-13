import numpy as np

def internal_rate_of_return(cash_flows):
    """
    Calculate Internal Rate of Return (IRR).

    IRR is the discount rate that makes the NPV of all cash flows from a particular project equal to zero. It's used to evaluate the attractiveness of a project or investment.

    :param cash_flows: List of cash flows (inflows and outflows).
    :return: IRR value.
    """
    return np.irr(cash_flows)

# Example usage:
cash_flows = [-500, 200, 300, 400]
print(internal_rate_of_return(cash_flows))
