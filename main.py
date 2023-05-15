class ItemToPurchase:
    
    def __init__(self):
        self.item_name = "none"
        self.item_price = 0
        self.item_quantity = 0
        
    def print_item_cost(self):
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_price*self.item_quantity}")
        

if __name__ == "__main__":

    item1 = ItemToPurchase()
    print("Item 1")
    item1.item_name = input("Enter the item name:\n")
    item1.item_price = int(input("Enter the item price:\n"))
    item1.item_quantity = int(input("Enter the item quantity:\n"))
    print()

    item2 = ItemToPurchase()
    print("Item 2")
    item2.item_name = input("Enter the item name:\n")
    item2.item_price = int(input("Enter the item price:\n"))
    item2.item_quantity = int(input("Enter the item quantity:\n"))
    print()

    print("TOTAL COST")
    item1.print_item_cost()
    item2.print_item_cost()
    total_cost = item1.item_price*item1.item_quantity + item2.item_price*item2.item_quantity
    print(f"\nTotal: ${total_cost}")

class ItemToPurchase:
    def __init__(self):
        self.item_name = "none"
        self.item_price = 0
        self.item_quantity = 0
        self.item_description = "none"
        
    def print_item_cost(self):
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_price*self.item_quantity}")
    
    def print_item_description(self):
        print(f"{self.item_name}: {self.item_description}")

class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2016"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []
    
    def add_item(self, item):
        self.cart_items.append(item)
    
    def remove_item(self, item_name):
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                return
        print("Item not found in cart. Nothing removed.")
    
    def modify_item(self, item):
        for i in range(len(self.cart_items)):
            if self.cart_items[i].item_name == item.item_name:
                self.cart_items[i].item_quantity = item.item_quantity
                return
        print("Item not found in cart. Nothing modified.")
    
    def get_num_items_in_cart(self):
        num_items = 0
        for item in self.cart_items:
            num_items += item.item_quantity
        return num_items
    
    def get_cost_of_cart(self):
        total_cost = 0
        for item in self.cart_items:
            total_cost += item.item_quantity * item.item_price
        return total_cost
    
    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        num_items = self.get_num_items_in_cart()
        print(f"Number of Items: {num_items}\n")
        if num_items == 0:
            print("SHOPPING CART IS EMPTY")
            return
        total_cost = self.get_cost_of_cart()
        for item in self.cart_items:
            item.print_item_cost()
        print(f"\nTotal: ${total_cost}")
    
    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}\n")
        print("Item Descriptions")
        for item in self.cart_items:
            item.print_item_description()
            print()
if __name__ == "__main__":

    customer_name = input("Enter customer's name:\n")
    current_date = input("Enter today's date:\n")


    print("\nCustomer name:", customer_name)
    print("Today's date:", current_date)

 
    shopping_cart = ShoppingCart(customer_name, current_date)

def print_menu():
    print("\nMENU")
    print("a - Add item to cart")
    print("r - Remove item from cart")
    print("c - Change item quantity")
    print("i - Output items' descriptions")
    print("o - Output shopping cart")
    print("q - Quit")
def execute_menu(choice, cart):
    if choice == 'a':
        item = ItemToPurchase()
        item.item_name = input("Enter the item name:\n")
        item.item_description = input("Enter the item description:\n")
        item.item_price = int(input("Enter the item price:\n"))
        item.item_quantity = int(input("Enter the item quantity:\n"))
        cart.add_item(item)
    elif choice == 'r':
        item_name = input("Enter the name of the item to remove:\n")
        cart.remove_item(item_name)
    elif choice == 'c':
        item = ItemToPurchase()
        item.item_name = input("Enter the item name:\n")
        item.item_quantity = int(input("Enter the new quantity:\n"))
        cart.modify_item(item)
    elif choice == 'i':
        cart.print_descriptions()
    elif choice == 'o':
        cart.print_total()
    elif choice == 'q':
        print("Exiting program...")
    else:
        print("Invalid menu choice. Please try again.")

cart = ShoppingCart(input("Enter customer's name: "), input("Enter today's date: "))
print("Customer name:", cart.customer_name)
print("Today's date:", cart.current_date)

choice = ''
while choice != 'q':
    print_menu()
    choice = input("Choose an option: ")
    execute_menu(choice, cart)
def execute_menu(choice, cart):
    if choice == 'a':
        item = ItemToPurchase()
        item.item_name = input("Enter the item name:\n")
        item.item_description = input("Enter the item description:\n")
        item.item_price = int(input("Enter the item price:\n"))
        item.item_quantity = int(input("Enter the item quantity:\n"))
        cart.add_item(item)
    elif choice == 'r':
        item_name = input("Enter the name of the item to remove:\n")
        cart.remove_item(item_name)
    elif choice == 'c':
        item = ItemToPurchase()
        item.item_name = input("Enter the item name:\n")
        item.item_quantity = int(input("Enter the new quantity:\n"))
        cart.modify_item(item)
    elif choice == 'i':
        cart.print_descriptions()
    elif choice == 'o':
        print("OUTPUT SHOPPING CART")
        cart.print_cart()
    elif choice == 'q':
        print("Exiting program...")
    else:
        print("Invalid menu choice. Please try again.")
def execute_menu(choice, cart):
    if choice == 'a':
        item = ItemToPurchase()
        item.item_name = input("Enter the item name:\n")
        item.item_description = input("Enter the item description:\n")
        item.item_price = int(input("Enter the item price:\n"))
        item.item_quantity = int(input("Enter the item quantity:\n"))
        cart.add_item(item)
    elif choice == 'r':
        item_name = input("Enter the name of the item to remove:\n")
        cart.remove_item(item_name)
    elif choice == 'c':
        item = ItemToPurchase()
        item.item_name = input("Enter the item name:\n")
        item.item_quantity = int(input("Enter the new quantity:\n"))
        cart.modify_item(item)
    elif choice == 'i':
        cart.print_descriptions()
    elif choice == 'o':
        cart.print_total()
    elif choice == 'q':
        print("Exiting program...")
    else:
        print("Invalid menu choice. Please try again.")

def execute_menu(choice, cart):
    if choice == 'a':
        item = ItemToPurchase()
        item.item_name = input("Enter the item name:\n")
        item.item_description = input("Enter the item description:\n")
        item.item_price = int(input("Enter the item price:\n"))
        item.item_quantity = int(input("Enter the item quantity:\n"))
        cart.add_item(item)
    elif choice == 'r':
        item_name = input("Enter the name of the item to remove:\n")
        cart.remove_item(item_name)
    elif choice == 'c':
        item = ItemToPurchase()
        item.item_name = input("Enter the item name:\n")
        item.item_quantity = int(input("Enter the new quantity:\n"))
        cart.modify_item(item)
    elif choice == 'i':
        cart.print_descriptions()
    elif choice == 'o':
        cart.print_total()
    elif choice == 'q':
        print("Exiting program...")
    else:
        print("Invalid menu choice. Please try again.")
        
def main():

    customer_name = input("Enter customer's name:\n")
    current_date = input("Enter today's date:\n")

    print("\nCustomer name:", customer_name)
    print("Today's date:", current_date)

    new_cart = ShoppingCart(customer_name, current_date)

    print_menu()

    while True:
        choice = input("Choose an option:\n")
        if choice == 'q':
            execute_menu(choice, new_cart)
            break
        elif choice in ['a', 'r', 'c', 'i', 'o']:
            execute_menu(choice, new_cart)
        else:
            print("Invalid menu choice. Please try again.")
            print_menu()

if __name__ == "__main__":
    main()
