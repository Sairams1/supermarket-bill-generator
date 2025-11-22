from datetime import datetime

name = input("Enter your name: ")

# items: name -> (price_per_unit, unit)
items = {
    'rice':    (20,  'kg'),
    'sugar':   (30,  'kg'),
    'salt':    (20,  'kg'),
    'oil':     (80,  'liter'),
    'paneer':  (110, 'kg'),
    'maggi':   (50,  'kg'),
    'boost':   (90,  'each'),
    'colgate': (85,  'each')
}

print("\nAvailable items:\n")
print(f"{'Item':<10}{'Price':<10}{'Unit'}")
print("-" * 30)
for name_i, (price, unit) in items.items():
    print(f"{name_i.capitalize():<10}Rs {price:<7}{unit}")
print("-" * 30)

pricelist = []   # list of (item, quantity, price)
totalprice = 0

def get_quantity(unit):
    raw = input(f"Enter quantity in {unit} (e.g. 2 or 2{unit}): ").strip().lower()
    num = ""
    for ch in raw:
        if ch.isdigit():
            num += ch
        elif num:
            break
        else:
            if ch == ' ':
                continue
            else:
                break
    if not num:
        return None
    return int(num)

def find_item(user_text):
    user_text = user_text.strip().lower()
    if user_text in items:
        return user_text

    matches = [name for name in items if name.startswith(user_text)]
    if len(matches) == 1:
        print(f"Matched '{user_text}' to '{matches[0]}'")
        return matches[0]
    elif len(matches) > 1:
        print("Multiple items match, be more specific: ", ", ".join(matches))
        return None
    else:
        print("No item found starting with that text.")
        return None

while True:
    print("\n1. Buy item")
    print("2. Bill & Exit")
    choice = input("Choose 1 or 2: ").strip()

    if choice == '2':
        break
    if choice != '1':
        print("Invalid option, please choose 1 or 2.")
        continue

    user_item = input("Enter item name or starting letters: ")
    item = find_item(user_item)
    if item is None:
        continue

    price_per_unit, unit = items[item]
    quantity = get_quantity(unit)
    if quantity is None or quantity <= 0:
        print("Invalid quantity.")
        continue

    price = quantity * price_per_unit
    pricelist.append((item, quantity, price, unit))
    totalprice += price
    print(f"Added {quantity} {unit} of {item} = Rs {price}")

if totalprice == 0:
    print("\nNo items purchased.")
else:
    gst = totalprice * 0.05
    finalamount = totalprice + gst

    print("\n" + "=" * 25, "KIRAN SUPERMARKET", "=" * 25)
    print(" " * 28, "WANAPARTHY")
    now = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    print(f"Name: {name:20} Date: {now}")
    print("-" * 70)
    print(f"{'S.No':<6}{'Item':<12}{'Qty':<12}{'Price':>10}")
    print("-" * 70)

    for i, (item, qty, price, unit) in enumerate(pricelist, start=1):
        qty_with_unit = f"{qty} {unit}"
        print(f"{i:<6}{item:<12}{qty_with_unit:<12}{price:>10}")

    print("-" * 70)
    print(f"{'Total Amount:':<30} Rs {totalprice:.2f}")
    print(f"{'GST (5%):':<30} Rs {gst:.2f}")
    print("-" * 70)
    print(f"{'FINAL AMOUNT:':<30} Rs {finalamount:.2f}")
    print("-" * 70)
    print(" " * 20, "Thanks for visiting!")
    print("-" * 70)
