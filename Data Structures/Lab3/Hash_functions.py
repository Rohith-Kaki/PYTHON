class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        # Simple hash function using the length of the key
        return len(key) % self.size

    def rehash(self):
        # Double the size of the table and rehash all entries
        self.size *= 2
        old_table = self.table
        self.table = [None] * self.size
        for entry in old_table:
            if entry:
                for product in entry:
                    self.add_product(product)

    def add_product(self, product):
        key = product.name
        index = self.hash_function(key)
        if self.table[index] is None:
            self.table[index] = [(key, product)]
        else:
            for i, (existing_key, _) in enumerate(self.table[index]):
                if existing_key == key:
                    # Product with the same name already exists, update it
                    self.table[index][i] = (key, product)
                    return
            # Collision handling: add to the existing list at the same index
            self.table[index].append((key, product))
        # Check for load factor and rehash if needed
        load_factor = sum(1 for bucket in self.table if bucket) / self.size
        if load_factor > 0.7:
            self.rehash()

    def search_product(self, product_name):
        index = self.hash_function(product_name)
        bucket = self.table[index]
        if bucket:
            for key, product in bucket:
                if key == product_name:
                    return product
        return None

# Example usage:
if __name__ == "__main__":
    # Create a hash table
    hash_table = HashTable()
    # Add products to the hash table
    hash_table.add_product(Product("Laptop", 999.99))
    hash_table.add_product(Product("Smartphone", 599.99))
    hash_table.add_product(Product("Headphones", 89.99))
    hash_table.add_product(Product("Tablet", 299.99))
    # Search for products in the hash table
    search_result = hash_table.search_product("Laptop")
    if search_result:
        print(f"Product found: {search_result.name} - Price: {search_result.price}")
    else:
        print("Product not found.")