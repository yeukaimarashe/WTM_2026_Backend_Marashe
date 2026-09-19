# 1. Interactive Terminal E-Commerce Cart & Inventory Tracker

# Available inventory: Item Name -> Unit Price
catalog = {
    "laptop": 800,
    "mouse": 20,
    "keyboard": 50,
    "monitor": 150
}

grand_total = 0

while True:
    action = input(
        "Enter item to buy (or 'checkout' / 'exit'): ").lower()

    if action == "exit":
        print("--> Order cancelled. No items were purchased.")
        break

    elif action == "checkout":
        # Apply conditional discounts based on grand_total
        if grand_total >= 500:
            discount_rate = 0.10
        elif grand_total >= 200:
            discount_rate = 0.05
        else:
            discount_rate = 0.0

        discount_amount = grand_total * discount_rate
        final_total = grand_total - discount_amount

        print("\nCHECKOUT RECEIPT")
        print("=" * 40)
        print(f"Subtotal: ${grand_total:.2f}")
        print(f"Discount: ${discount_amount:.2f}")
        print(f"Final Total: ${final_total:.2f}")
        print("=" * 40)
        break

    elif action in catalog:
        price = catalog[action]
        grand_total += price
        print(f"--> Added {action.title()} ({price}) to order.")

    else:
        print("--> [ERROR] Item not found in catalog. Try again.")
