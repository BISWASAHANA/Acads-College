#include <stdio.h>
#include <stdlib.h>

// Custom data structure to represent a node in the linked list
typedef struct Node {
    int data;
    struct Node *next;
} Node;

// Function to create a new node
Node* createNode(int data) {
    Node *newNode = (Node *)malloc(sizeof(Node));
    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}

// Function to insert a node at the beginning of the linked list
Node* insertAtBeginning(Node *head, int data) {
    Node *newNode = createNode(data);
    newNode->next = head;
    return newNode;
}

// Function to display the linked list
void displayList(Node *head) {
    Node *current = head;
    while (current != NULL) {
        printf("%d -> ", current->data);
        current = current->next;
    }
    printf("NULL\n");
}

// Function to free memory used by the linked list
void freeList(Node *head) {
    Node *current = head;
    while (current != NULL) {
        Node *temp = current;
        current = current->next;
        free(temp);
    }
}

int main() {
    Node *head = NULL;
    int choice, data;

    while (1) {
        printf("\nLinked List Operations Menu:\n");
        printf("1. Insert at the beginning\n");
        printf("2. Display the list\n");
        printf("3. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                printf("Enter data to insert: ");
                scanf("%d", &data);
                head = insertAtBeginning(head, data);
                printf("Node inserted at the beginning.\n");
                break;
            case 2:
                printf("Linked List: ");
                displayList(head);
                break;
            case 3:
                freeList(head);
                printf("Exiting the program.\n");
                exit(0);
            default:
                printf("Invalid choice! Please try again.\n");
        }
    }

    return 0;
}
#include <stdio.h>
#include <stdlib.h>

// Custom data structure to represent a node in the linked list
typedef struct Node {
    int data;
    struct Node *next;
} Node;

// Function to create a new node
Node* createNode(int data) {
    Node *newNode = (Node *)malloc(sizeof(Node));
    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}

// Function to insert a node at the beginning of the linked list
Node* insertAtBeginning(Node *head, int data) {
    Node *newNode = createNode(data);
    newNode->next = head;
    return newNode;
}

// Function to display the linked list
void displayList(Node *head) {
    Node *current = head;
    while (current != NULL) {
        printf("%d -> ", current->data);
        current = current->next;
    }
    printf("NULL\n");
}

// Function to free memory used by the linked list
void freeList(Node *head) {
    Node *current = head;
    while (current != NULL) {
        Node *temp = current;
        current = current->next;
        free(temp);
    }
}

int main() {
    Node *head = NULL;
    int choice, data;

    while (1) {
        printf("\nLinked List Operations Menu:\n");
        printf("1. Insert at the beginning\n");
        printf("2. Display the list\n");
        printf("3. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                printf("Enter data to insert: ");
                scanf("%d", &data);
                head = insertAtBeginning(head, data);
                printf("Node inserted at the beginning.\n");
                break;
            case 2:
                printf("Linked List: ");
                displayList(head);
                break;
            case 3:
                freeList(head);
                printf("Exiting the program.\n");
                exit(0);
            default:
                printf("Invalid choice! Please try again.\n");
        }
    }

    return 0;
}
