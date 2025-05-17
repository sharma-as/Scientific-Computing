def calculate_volume(length, width, height):
    """
    Calculate the volume of a rectangular box.
    
    Parameters:
    length (float): The length of the box.
    width (float): The width of the box.
    height (float): The height of the box.
    
    Returns:
    float: The volume of the box.
    """
    return length * width * height

# Test cases
dimensions = [
    (3, 4, 5),  # Length = 3, Width = 4, Height = 5
    (10, 2, 8), # Length = 10, Width = 2, Height = 8
    (7.5, 3.2, 4.1), # Length = 7.5, Width = 3.2, Height = 4.1
    (1, 1, 1),  # Length = 1, Width = 1, Height = 1
    (0, 5, 7),  # Length = 0, Width = 5, Height = 7 (expect volume = 0)
]

# Calculate and print the volume for each set of dimensions
for length, width, height in dimensions:
    volume = calculate_volume(length, width, height)
    print(f"Volume of box with Length = {length}, Width = {width}, Height = {height} is {volume:.2f} cubic units.")