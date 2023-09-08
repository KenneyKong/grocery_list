def main():
    grocery_list = {}

    print("Welcome to the Grocery List Maker!")

    while True:
        try:
            item = input("Enter an item (or press Ctrl-D to finish): ").strip()
            if not item:
                break

            item_lower = item.lower()

            if item_lower in grocery_list:
                grocery_list[item_lower] += 1
            else:
                grocery_list[item_lower] = 1

        except EOFError:
            break

    sorted_items = sorted(grocery_list.keys())
    print("\nYour Grocery List:")
    for item in sorted_items:
        count = grocery_list[item]
        print(f"{count} {item.upper()}")

    print("Thank you for creating your grocery list!")

if __name__ == "__main__":
    main()
