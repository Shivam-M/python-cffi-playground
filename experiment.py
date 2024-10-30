from cffi import FFI

ffi = FFI()

with open("header.h", "r") as header:
    ffi.cdef(header.read())

with open("source.c", "r") as source:
    ffi.set_source("_test", source.read())

ffi.compile()

###

import _test

_test.lib.initialise()

shivam = _test.ffi.new("struct Person *")
shivam.name = _test.ffi.new("char[]", b"Shivam")
shivam.age = 22

shivam_clone = _test.ffi.new("struct Person *")
shivam_clone.name = _test.ffi.cast("const char *", _test.ffi.new("char[]", b"Shivam Clone"))
shivam_clone.age = 22

random_person = _test.lib.getPerson()

list_of_people = _test.lib.createList()

_test.lib.appendList(list_of_people, shivam)
_test.lib.appendList(list_of_people, shivam_clone)
_test.lib.appendList(list_of_people, random_person)

for x in range(5):
    _test.lib.appendList(list_of_people, _test.lib.getPerson())

# _test.lib.removeList(list_of_people, shivam_clone)

current_node = list_of_people.head
while current_node:
    person = current_node.data
    print(f"Name: {_test.ffi.string(person.name).decode()}, Age: {person.age}")
    current_node = current_node.next

_test.lib.freeList(list_of_people)

# print(f"Name: {ffi.string(shivam.name).decode()}, Age: {shivam.age}")
# print(f"Name: {ffi.string(random_person.name).decode()}, Age: {random_person.age}")
