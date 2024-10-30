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

struct Node* createNode(struct Person*);
struct LinkedList* createList();
struct Person* createPerson(char*, int);
struct Person* getPerson();

void freePerson(struct Person*);
void freeNode(struct Node*);
void freeList(struct LinkedList*);
void appendList(struct LinkedList*, struct Person*);
void removeList(struct LinkedList*, struct Person*);
void initialise();
