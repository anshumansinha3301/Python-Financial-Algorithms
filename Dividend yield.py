def dividend_yield(dividend_per_share, market_price_per_share):
    """
    Calculate Dividend Yield.

    The dividend yield is a financial ratio that shows how much a company pays out in dividends each year relative to its stock price. It's used by investors to evaluate the return on their investment.

    :param dividend_per_share: Dividend paid per share.
    :param market_price_per_share: Current market price per share.
    :return: Dividend yield as a percentage.
    """
    return (dividend_per_share / market_price_per_share) * 100

# Example usage:
dividend_per_share = 2
market_price_per_share = 50
print(dividend_yield(dividend_per_share, market_price_per_share))
