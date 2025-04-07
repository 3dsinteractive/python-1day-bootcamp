"""
This module demonstrates basic arithmetic operations in Python.
"""

def main():
    """This function performs and prints the results of various arithmetic operations."""
    print(1+1)
    print(7/4)
    print(7%4)

    my_int: int = 10
    print(my_int)
    my_other_int = my_int
    my_int = "450"
    print(my_other_int)
    print(my_int)

    # my_plus_int = my_int + my_other_int
    # print(my_plus_int)

    my_dogs = ["Rex", "Fido"]
    print(my_dogs)

    print(type(my_dogs))

    my_string = "Hello"
    my_string = my_string + " World"
    print(my_string)

    name = "Alice"
    greeting = f"Hello, {name}!"
    print(greeting)

    my_list = [1, 2, 3]
    my_list[0] = 0
    print(my_list)

    multi_type_list = [1, "Hello", 3.14]
    print(multi_type_list)
    print(len(multi_type_list))

    first_list = [1, 2, 3]
    second_list = [4, 5, 6]
    combined_list = first_list + second_list
    combined_list.append(7)
    print(combined_list)

    combined_list.pop()
    print(combined_list)

    combined_list2 = combined_list
    combined_list2.append(8)
    print(combined_list)

    numbers = [3, 2, 1]
    numbers.sort()
    print(numbers)
    numbers.reverse()
    print(numbers)

    my_dict = {"name": "Alice", "age": 30}
    print(my_dict)
    print(my_dict["name"])
    my_dict["gender"] = "Female"
    print(my_dict)
    my_dict["properties"] = {"height": 170, "weight": 60}
    print(my_dict["properties"]["height"])

    my_tuple = (1, 2, 2, 5, 3)
    print(my_tuple)
    print(my_tuple.index(2))
    print(my_tuple.count(2))

    my_set = {1, 2, 3, 4, 5}
    print(type(my_set))
    my_set.add(6)
    print(my_set)

    str_list = ["Hello", "World", "Hello", "World"]
    str_set = set(str_list)
    print(str_set)
    str_set.add("Python")
    print(str_set)
    str_set.remove("Hello")
    print(str_set)

    my_bool: bool = True
    print(my_bool)
    print(type(my_bool))
    my_bool = False
    print(my_bool)
    print(type(my_bool))
    my_bool = None
    print(my_bool)
    print(type(my_bool))

if __name__ == "__main__":
    main()
