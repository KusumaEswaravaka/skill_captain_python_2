class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        return f"Product Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}"

# Function to register a product
def register_product():
    name = input("Enter the product name: ")
    price = float(input("Enter the product price: "))
    quantity = int(input("Enter the product quantity: "))
    return Product(name, price,quantity)
    

# Database to store registered products
product_database = []


# Main function to interact with the user
def main():
    while True:
        print("\nProduct Registration System")
        print("1. Register a new product")
        print("2. Display all products")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            product = register_product()
            product_database.append(product)
            print("Product registered successfully!")
        elif choice == '2':
            if product_database:
                print(product.display_info())
            else:
                print("No products registered.")
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")


main()
