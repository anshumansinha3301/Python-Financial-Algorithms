def return_on_investment(gain_from_investment, cost_of_investment):
    """
    Calculate Return on Investment (ROI).

    ROI is a measure used to evaluate the efficiency or profitability of an investment. It is calculated by dividing the gain from the investment by the cost of the investment.

    :param gain_from_investment: Profit from investment.
    :param cost_of_investment: Cost of the investment.
    :return: ROI as a percentage.
    """
    roi = (gain_from_investment - cost_of_investment) / cost_of_investment * 100
    return roi

# Example usage:
gain_from_investment = 2000
cost_of_investment = 1500
print(return_on_investment(gain_from_investment, cost_of_investment))
