# Expense Tracker + installment 2, Author: John Marich J. Castro


installment_version = "2.0.0"
line_count = 40
menu_items = ["Add Expense", "View All Expenses", "Show Total Expenses", "Exit"]

#Input variables
name: str
item1:str
item2: str
amount1: float
amount2: float


print("="*line_count)
print("\t\tEXPENSE TRACKER")
print("\tKnow where your money goes")
print("="*line_count)
print("\nWelcome! this is your personal expense tracker\n")

print("MAIN MENU")
for i, item in enumerate(menu_items, start=1):
    print(f"  [{i}] {item:<22}(coming soon)")

# ask name

name = input("What's your name? ")
print(f"Welcome, {name}! Let's log two expenses")

# ask expenses
item1 = input("First expense? ")
amount1 = float(input("Amount? "))
item2 = input("Second expense? ")
amount2 = float(input("Amount? "))

total: float = amount1 + amount2
average = float(total)/2

amount1_text = f"${amount1:.2f}"
amount2_text = f"${amount2:.2f}"
total_text = f"${total:.2f}"
average_text = f"${average:.2f}"


print(f"\n{'-' * line_count}")
print("SUMMARY")
print(f"{item1:<20}{amount1_text:>10}")
print(f"{item2:<20}{amount2_text:>10}")
print(f"{'Total spent:':<20}{total_text:>10}")
print(f"{'Average:':<20}{average_text:>10}")
print("-"*line_count)
print(f"Made by: John Marich J. Castro | Installment {installment_version} | 2026")
print("="*line_count)
