from dataclasses import dataclass


class Info:
    # class variable. This mainly is used as a default and it can easily be overwritten by
    # an instance variable with the same name silently
    body = "test"

    def __init__(self, data: str = ""):
        if data != "":
            self.body = data

    def setBody(self, data: str):
        Info.body = data


a = Info()
b = Info()

# These are accessing the class variable
print(a.body)
print(b.body)

# These are creating instance variables dynamically without changing the class variable
a.body = "test-a"
b.body = "test-b"

# Now these are the instance variables
print(a.body)
print(b.body)

# This is accessing the original class variable
print(Info.body)

# These are setting the class variable
a.setBody("test-a-2")
b.setBody("test-b-2")
print(a.body)
print(b.body)
print(Info.body)


def passByReferenceTest(a: Info):
    a = Info("test2")


def passByPointerTest(a: Info):
    a.body = "test2"


a = Info("test1")
print(a.body)
passByReferenceTest(a)
# a still has "test1", so python does not pass by reference
print(a.body)

passByPointerTest(a)
# a has "test2", so python pass by pointer and the pointer is passed by value just like java
print(a.body)
