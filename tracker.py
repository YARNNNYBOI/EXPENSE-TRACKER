
installment_version = "1.0.0"
line_count = 40
menu_items = ["Add Expense", "View All Expenses", "Show Total Expenses", "Exit"]

print("="*line_count)
print("\t    EXPENSE TRACKER")
print("\tKnow where your money goes")
print("="*line_count)
print("\nWelcome! this is your personal expense tracker\n")

print("MAIN MENU")
for i, item in enumerate(menu_items, start=1):
    print(f"  [{i}] {item:<22}(coming soon)")


print("-"*line_count)
print(f"Made by: John Marich J. Castro | Installment {installment_version} | 2024")
print("="*line_count)