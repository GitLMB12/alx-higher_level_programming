#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    nb_print = 0
    try:
        for i in range x:
            print(my_list[i], end="")
            nb_print += 1
    except IndexError:
        pass
    print()
    return nb_print
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    safe_print_list(my_list)
