def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.

    Args:
        price (float): Original price.
        discount_percent (float): Discount percentage.

    Returns:
        float: Final price after applying the discount.
    """
    if discount_percent >= 20:
        # Apply the discount
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
    else:
        # No discount applied
        final_price = price
    return final_price

# Prompt user for input
original_price = float(input("Enter the original price: "))
discount_percentage = float(input("Enter the discount percentage: "))

# Calculate the final price
final_price = calculate_discount(original_price, discount_percentage)

# Print the result
print(f"Final price after applying the discount: ${final_price:.2f}")
