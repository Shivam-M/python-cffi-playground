#include <stdint.h>

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

void freeNode(struct Node*);
void freeList(struct LinkedList*);
void appendList(struct LinkedList*, struct Person*);
void removeList(struct LinkedList*, struct Person*);
void initialise();
