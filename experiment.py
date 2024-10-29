from cffi import FFI

ffi = FFI()

ffi.cdef("""
    struct Person {
        const char* name;
        uint8_t age;
    };
    
    struct Node {
        struct Person* data;
        struct Node* next;
    };

    struct LinkedList {
        struct Node* head;
    };

    struct Node* createNode(struct Person*);
    struct Person* getPerson();
    struct LinkedList* createList();

    void appendList(struct LinkedList*, struct Person*);
    
""")

ffi.set_source(
    "_test", 
    """
    #include <stdint.h>
    #include <stdlib.h>

    struct Person {
        const char* name;
        uint8_t age;
    };

    struct Node {
        struct Person* data;
        struct Node* next;
    };

    struct LinkedList {
        struct Node* head;
    };

    struct Person* getPerson() {
        struct Person* person = (struct Person*) malloc(sizeof(struct Person));
        if (person == NULL) return NULL;

        person->name = "Random Person";
        person->age = (rand() % 100) + 1;
        return person;
    };

    struct Node* createNode(struct Person* person) {
        struct Node* node = (struct Node*) malloc(sizeof(struct Node));
        if (node == NULL) return NULL;

        node->data = person;
        node->next = NULL;
        return node;
    }

    struct LinkedList* createList() {
        struct LinkedList* linked_list = (struct LinkedList*) malloc(sizeof(struct LinkedList));
        if (linked_list == NULL) return NULL;

        linked_list->head = NULL;
        return linked_list;
    };

    void appendList(struct LinkedList* linked_list, struct Person* person) {
        struct Node* new_node = createNode(person);

        if (linked_list->head == NULL) {
            linked_list->head = new_node;
        } else {
            struct Node* current_node = linked_list->head;
            while (current_node->next != NULL) {
                current_node = current_node->next;
            }
            current_node->next = new_node;
        }
    }
    
    """
)

ffi.compile()

###

import _test

shivam = _test.ffi.new("struct Person *")
shivam.name = _test.ffi.new("char[]", b"Shivam")
shivam.age = 22

random_person = _test.lib.getPerson()

list_of_people = _test.lib.createList()

_test.lib.appendList(list_of_people, shivam)
_test.lib.appendList(list_of_people, random_person)

current_node = list_of_people.head
while current_node != ffi.NULL:
    person = current_node.data
    print(f"Name: {ffi.string(person.name).decode()}, Age: {person.age}")
    current_node = current_node.next

# print(f"Name: {ffi.string(shivam.name).decode()}, Age: {shivam.age}")
# print(f"Name: {ffi.string(random_person.name).decode()}, Age: {random_person.age}")
