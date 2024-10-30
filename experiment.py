from cffi import FFI

ffi = FFI()

with open("header.h", "r") as header:
    ffi.cdef(header.read())

with open("source.c", "r") as source:
    ffi.set_source("_test", source.read())

ffi.compile()

###

from definitions import LinkedList, Person
import _test

_test.lib.initialise()

linked_list = LinkedList()

batman = _test.ffi.new("struct Person *")
batman.name = _test.ffi.new("char[]", b"Batman")
batman.age = 32

alfred = _test.ffi.new("struct Person *")
alfred.name = _test.ffi.new("char[]", b"Alfred")
alfred.age = 65

robin = Person("Robin", 30)

linked_list.append(batman)
linked_list.append(alfred)
linked_list.append(robin._get())

for x in range(5):
    linked_list.append(_test.lib.getPerson())

# linked_list.remove(robin._get())

for item in linked_list:
    print(_test.ffi.string(item.name).decode(), item.age)

del linked_list

# print(batman)

###

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
