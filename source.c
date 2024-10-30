#include <stdint.h>
#include <stdlib.h>
#include <time.h>

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
}

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
}

void freeNode(struct Node* node) {
    free(node->data);
    free(node);
}

void freeList(struct LinkedList* linked_list) {
    struct Node* current_node = linked_list->head;
    while (current_node) {
        struct Node* next_node = current_node->next;
        freeNode(current_node);
        current_node = next_node;
    }
    free(linked_list);
}

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

void removeList(struct LinkedList* linked_list, struct Person* person) {
    struct Node* current_node = linked_list->head;
    struct Node* previous_node = NULL;

    while (current_node != NULL) {
        if (current_node->data == person) {
            if (previous_node == NULL) {
                linked_list->head = current_node->next;
            } else {
                previous_node->next = current_node->next;
            }
            freeNode(current_node);
            return;
        }
        previous_node = current_node;
        current_node = current_node->next;
    }
}

void initialise() {
    srand(time(NULL));
}
