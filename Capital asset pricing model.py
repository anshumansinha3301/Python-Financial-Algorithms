def capm(expected_market_return, risk_free_rate, beta):
    """
    Calculate Expected Return using Capital Asset Pricing Model (CAPM).

    CAPM describes the relationship between systematic risk and expected return for assets, particularly stocks.

    :param expected_market_return: Expected return of the market.
    :param risk_free_rate: Risk-free rate of return.
    :param beta: Beta of the security.
    :return: Expected return of the security.
    """
    return risk_free_rate + beta * (expected_market_return - risk_free_rate)

# Example usage:
expected_market_return = 0.08
risk_free_rate = 0.03
beta = 1.2
print(capm(expected_market_return, risk_free_rate, beta))
