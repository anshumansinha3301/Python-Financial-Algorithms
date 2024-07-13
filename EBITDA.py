def ebitda(revenue, expenses, interest, taxes, depreciation, amortization):
    """
    Calculate Earnings Before Interest, Taxes, Depreciation, and Amortization (EBITDA).

    EBITDA is a measure of a company's overall financial performance and is used as an alternative to net income.

    :param revenue: Total revenue.
    :param expenses: Operating expenses.
    :param interest: Interest expenses.
    :param taxes: Tax expenses.
    :param depreciation: Depreciation expenses.
    :param amortization: Amortization expenses.
    :return: EBITDA value.
    """
    return revenue - expenses + interest + taxes + depreciation + amortization

# Example usage:
revenue = 100000
expenses = 60000
interest = 5000
taxes = 10000
depreciation = 8000
amortization = 7000
print(ebitda(revenue, expenses, interest, taxes, depreciation, amortization))
