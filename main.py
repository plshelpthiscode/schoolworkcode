class ItemToPurchase:
    def __init__(self):
        self.item_name = "none"
        self.item_price = 0
        self.item_quantity = 0
        self.item_description = "none" 

    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${total_cost}")

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
        for i, cart_item in enumerate(self.cart_items):
            if cart_item.item_name == item.item_name:
                self.cart_items[i] = item
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
            total_cost += item.item_price * item.item_quantity
        return total_cost

    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        num_items = self.get_num_items_in_cart()
        print(f"Number of Items: {num_items}\n")

        if num_items == 0:
            print("SHOPPING CART IS EMPTY")
            return

        total_cost = 0
        for item in self.cart_items:
            item_cost = item.item_price * item.item_quantity
            total_cost += item_cost
            item.print_item_cost()

        print(f"\nTotal: ${total_cost}")

    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}\n")
        print("Item Descriptions")
        for item in self.cart_items:
            item.print_item_description()
            print()

customer_name = input("Enter customer's name:\n")
today_date = input("Enter today's date:\n")


print("\nCustomer name:", customer_name)
print("Today's date:", today_date)


cart = ShoppingCart(customer_name, today_date)

def print_menu():
    print("MENU")
    print("a - Add item to cart")
    print("r - Remove item from cart")
    print("c - Change item quantity")
    print("i - Output items' descriptions")
    print("o - Output shopping cart")
    print("q - Quit")




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
