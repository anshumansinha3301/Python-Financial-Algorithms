def quick_ratio(current_assets, inventory, current_liabilities):
    """
    Calculate Quick Ratio.

    The quick ratio, also known as the acid-test ratio, measures a company's ability to meet its short-term obligations with its most liquid assets.

    :param current_assets: Total current assets.
    :param inventory: Total inventory.
    :param current_liabilities: Total current liabilities.
    :return: Quick ratio.
    """
    return (current_assets - inventory) / current_liabilities

# Example usage:
current_assets = 15000
inventory = 5000
current_liabilities = 5000
print(quick_ratio(current_assets, inventory, current_liabilities))
