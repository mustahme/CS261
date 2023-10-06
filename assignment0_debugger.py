# Name: Ahmed Mustafa
# OSU Email: MustaAhm@OregonState.edu
# Course: CS261 - Data Structures
# Assignment: Assignment 0
# Due Date: 09OCT2023
# Description: This will be used to verify GradeScope is working for CS261


# Please enter your name, favorite color, favorite hobby, and hometown in the list
my_list = ['Ahmed Mustafa', 'Blue', 'Hiking', 'Harrisonburg VA']

def my_info(my_list):
    """ A function that passes a list of my information """
    count = 0
    for value in my_list:
        count += 1
    return count


if __name__ == '__main__':
    print(my_info(my_list))

