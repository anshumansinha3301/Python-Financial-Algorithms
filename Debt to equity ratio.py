def debt_to_equity_ratio(total_debt, total_equity):
    """
    Calculate Debt-to-Equity Ratio.

    The debt-to-equity ratio is a measure of a company's financial leverage. It indicates what proportion of equity and debt the company is using to finance its assets.

    :param total_debt: Total debt of the company.
    :param total_equity: Total equity of the company.
    :return: Debt-to-equity ratio.
    """
    return total_debt / total_equity

# Example usage:
total_debt = 50000
total_equity = 200000
print(debt_to_equity_ratio(total_debt, total_equity))
