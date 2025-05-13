def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    Only apply the discount if it is 20% or higher.
    """
    if discount_percent >= 20:
        final_price = price - (price * (discount_percent / 100))
        return final_price
    else:
        return price

# Prompting the user to enter the original price and discount percentage
try:
    price = float(input("Enter the original price: "))
    discount_percent = float(input("Enter the discount percentage: "))

    # Calculating the final price using the function
    final_price = calculate_discount(price, discount_percent)

    # Displaying the result
    if final_price == price:
        print(f"No discount applied. The final price is: ${final_price:.2f}")
    else:
        print(f"Discount applied! The final price is: ${final_price:.2f}")

except ValueError:
    print("Invalid input. Please enter numerical values.")
