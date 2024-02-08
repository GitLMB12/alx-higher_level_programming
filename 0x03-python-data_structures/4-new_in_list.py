def new_in_list(my_list, idx, element):
    """Replace an element in a copied list at a specific position."""
    if idx < 0 or idx >= len(my_list):
        return my_list[:]  # Return a shallow copy of the original list

    my_list_copy = my_list[:]  # Create a shallow copy of the original list
    my_list_copy[idx] = element
    return my_list_copy
