#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            result = 0
            if i < len(my_list_1) and i < len(my_list_2):
                dividend = my_list_1[i]
                divisor = my_list_2[i]
                result = dividend / divisor
            elif i >= len(my_list_1) or i >= len(my_list_2):
                print("out of range")
            else:
                raise TypeError
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        finally:
            new_list.append(result)
    return new_list
