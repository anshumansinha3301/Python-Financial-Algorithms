import numpy as np

def simple_moving_average(prices, window):
    """
    Calculate the Simple Moving Average (SMA).

    SMA is used to smooth out price data to identify the direction of the trend.
    It's calculated by averaging a subset of prices over a defined period.

    :param prices: List of stock prices.
    :param window: Number of periods over which to average.
    :return: List of SMA values.
    """
    sma = np.convolve(prices, np.ones(window)/window, 'valid')
    return sma

# Example usage:
prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
window = 3
print(simple_moving_average(prices, window))
