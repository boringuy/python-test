from typing import List


class Data:
    def __init__(self, data: str = "", id: int = 0):
        self.__data = data
        self.__id = id
        self.__list = [id]

    def get_data(self) -> str:
        return self.__data

    def get_id(self) -> int:
        return self.__id

    def get_list(self) -> List[int]:
        return self.__list


# For immutable objects (like integers, strings, and tuples),
# Python behaves as if it is passing by value. When you return an immutable object,
# a new reference to the same object is created.

A = Data("test", 1)
id = A.get_id()
print(f"id: {id}")
print(f"A.id: {A.get_id()}")

id += 1

print(f"id: {id}")
print(f"A.id: {A.get_id()}")  # A.id is not changed

# For mutable objects (like lists, dictionaries, and sets),
# Python behaves more like passing by reference. When you return a mutable object,
# the reference to the same object is returned, and changes to the object will affect
# the original reference.

list1 = A.get_list()
list1.append(2)

print(f"list1: {list1}")
print(f"A.__list: {A.get_list()}")  # A.__list is modified outside of the class
