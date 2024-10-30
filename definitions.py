import _test


class LinkedList:
    def __init__(self):
        self._linked_list = _test.lib.createList()

    def __del__(self):
        _test.lib.freeList(self._linked_list)
    
    def __iter__(self):
        current_node = self._linked_list.head
        while current_node:
            yield current_node.data
            current_node = current_node.next
    
    def _get(self):
        return self._linked_list
    
    def append(self, data):
        _test.lib.appendList(self._linked_list, data)

    def remove(self, data):
        _test.lib.removeList(self._linked_list, data)


class Person:
    def __init__(self, name: str, age: int):
        self._person = _test.lib.createPerson(_test.ffi.new("char[]", name.encode()), age)
    
    def __del__(self):
        _test.lib.freePerson(self._person)

    def _get(self):
        return self._person

    def get_name(self) -> str:
        return _test.ffi.string(self._person.name).decode()
    
    def get_age(self) -> int:
        return self._person.age
