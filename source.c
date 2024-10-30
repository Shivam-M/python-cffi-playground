#include <stdint.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

static const char* RANDOM_NAMES[] = {
    "Bart", "Homer", "Lisa", "Marge", "Maggie", "Abe"
};
static const int RANDOM_NAMES_LENGTH = sizeof(RANDOM_NAMES) / sizeof(RANDOM_NAMES[0]);

struct Person {
    char* name;
    int age;
};

struct Node {
    struct Person* data;
    struct Node* next;
};

struct LinkedList {
    struct Node* head;
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
}

struct Person* createPerson(char* name, int age) {
    struct Person* person = (struct Person*) malloc(sizeof(struct Person));
    if (person == NULL) return NULL;

    person->name = strdup(name);
    person->age = age;
    return person;
}

struct Person* getPerson() {
    const char* name = RANDOM_NAMES[rand() % RANDOM_NAMES_LENGTH];
    int age = (rand() % 100) + 1;
    return createPerson(name, age);
}

void freePerson(struct Person* person) {
    if (person == NULL) return;
    // free(person->name);
    // free(person);
}

void freeNode(struct Node* node) {
    if (node == NULL) return;
    // free(node);
}

void freeList(struct LinkedList* linked_list) {
    if (linked_list == NULL) return;
    struct Node* current_node = linked_list->head;
    struct Node* next_node = NULL;

    while (current_node) {
        next_node = current_node->next;
        freePerson(current_node->data);
        freeNode(current_node);
        current_node = next_node;
    }

    // free(linked_list);
}

void appendList(struct LinkedList* linked_list, struct Person* person) {
    if (linked_list == NULL || person == NULL) return;
    struct Node* new_node = createNode(person);
    struct Node* current_node = NULL;
    if (linked_list->head) {
        current_node = linked_list->head;
        while (current_node->next) {
            current_node = current_node->next;
        }
        current_node->next = new_node;
    } else {
        linked_list->head = new_node;
    }
}

void removeList(struct LinkedList* linked_list, struct Person* person) {
    struct Node* current_node = linked_list->head;
    struct Node* previous_node = NULL;
    while (current_node) {
        if (current_node->data == person) {
            if (previous_node == NULL) {
                linked_list->head = current_node->next;
            } else {
                previous_node->next = current_node->next;
            }
            freePerson(current_node->data);
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
