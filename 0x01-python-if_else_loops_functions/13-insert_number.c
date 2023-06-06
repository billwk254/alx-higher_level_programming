#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * insert_node - Inserts a number into a sorted singly linked list
 * @head: Pointer to the head of the linked list
 * @number: Number to insert
 *
 * Return: Address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
listint_t *new_node, *current, *prev;

if (head == NULL)
return (0);

new_node = malloc(sizeof(listint_t));
if (new_node == NULL)
return (0);

new_node->n = number;
new_node->next = NULL;

if (*head == NULL)
{
*head = new_node;
return (new_node);
}

current = *head;
prev = NULL;

while (current != NULL && current->n < number)
{
prev = current;
current = current->next;
}

if (prev == NULL)
{
new_node->next = *head;
*head = new_node;
}
else
{
prev->next = new_node;
new_node->next = current;
}
return (new_node);
}
