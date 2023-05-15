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
