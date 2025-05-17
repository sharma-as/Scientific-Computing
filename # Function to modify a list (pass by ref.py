# Function to modify a list (pass by reference)
def modify_list_ref(my_list):
    print("Inside modify_list_ref (Before modification):", my_list)
    my_list.append(100)  # Modifying the original list
    print("Inside modify_list_ref (After modification):", my_list)

# Function to try modifying a copy of the list (pass by value)
def modify_list_val(my_list):
    print("Inside modify_list_val (Before modification):", my_list)
    my_list = my_list[:]  # Create a shallow copy of the list
    my_list.append(200)   # Modify the copy, not the original list
    print("Inside modify_list_val (After modification):", my_list)

# Main program
original_list = [1, 2, 3]

print("Original list before calling modify_list_ref:", original_list)
modify_list_ref(original_list)
print("Original list after calling modify_list_ref:", original_list)  # The original list is modified

print("\nOriginal list before calling modify_list_val:", original_list)
modify_list_val(original_list)
print("Original list after calling modify_list_val:", original_list)  # The original list remains unchanged