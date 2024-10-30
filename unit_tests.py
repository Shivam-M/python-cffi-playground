import _test
from definitions import LinkedList, Person


def test_create_person():
    test_person1 = Person("Test Person", 1)

    assert test_person1.get_name() == "Test Person"
    assert test_person1.get_age() == 1


def test_modify_person():
    test_person1 = Person("Test Person", 1)
    test_person1._get().name = _test.ffi.new("char[]", b"Changed Person")
    test_person1._get().age = 2

    assert test_person1.get_name() == "Changed Person"
    assert test_person1.get_age() == 2


def test_add_linkedlist():
    linked_list = LinkedList()

    linked_list.append(Person("Test Person", 1)._get())
    linked_list.append(Person("Test Person", 2)._get())
    linked_list.append(Person("Test Person", 3)._get())

    number_of_people = 0
    for _ in linked_list:
        number_of_people += 1
    
    assert number_of_people == 3


def test_add_remove_linkedlist():
    linked_list = LinkedList()
    
    test_person1 = Person("Test Person", 1)._get()
    test_person2 = Person("Test Person", 2)._get()
    test_person3 = Person("Test Person", 3)._get()

    linked_list.append(test_person1)
    linked_list.append(test_person2)
    linked_list.append(test_person3)

    linked_list.remove(test_person1)
    linked_list.remove(test_person2)
    linked_list.remove(test_person3)

    for _ in linked_list:
        raise AssertionError("Expected linked list to be empty")

    # assert linked_list._get().head == _test.ffi.NULL