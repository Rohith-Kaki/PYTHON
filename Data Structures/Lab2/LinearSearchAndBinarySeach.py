class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

def linear_search(dataset, target):
    """
    Linear search algorithm to find a product in the dataset.
    """
    for i, product in enumerate(dataset):
        if product.name == target:
            return i  # Return the index if found
    return -1  # Return -1 if not found

def binary_search(dataset, target):
    """
    Binary search algorithm to find a product in the sorted dataset.
    """
    low, high = 0, len(dataset) - 1
    while low <= high:
        mid = (low + high) // 2
        mid_product = dataset[mid].name
        if mid_product == target:
            return mid  # Return the index if found
        elif mid_product < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1  # Return -1 if not found

# Example usage:
if __name__ == "__main__":
    # Sample dataset (assuming it's a list of Product instances)
    dataset = [
        Product('earphones', 10.99),
        Product('mouse', 11.99),
        Product('heyboard', 12.99),
       
    ]

    # Perform linear search
    target_product = input("Enter target product:")
    linear_result = linear_search(dataset, target_product)
    if linear_result != -1:
        print(f"Linear Search: {target_product} found at index {linear_result}")
    else:
        print(f"Linear Search: {target_product} not found in the dataset")

    # Sort dataset for binary search (assuming the 'name' field is sortable)
    dataset.sort(key=lambda x: x.name)

    # Perform binary search
    binary_result = binary_search(dataset, target_product)
    if binary_result != -1:
        print(f"Binary Search: {target_product} found at index {binary_result}")
    else:
        print(f"Binary Search: {target_product} not found in the dataset")