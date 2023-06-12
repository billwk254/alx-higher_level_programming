#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * @head: Pointer to pointer to the head of the list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 * An empty list is considered a palindrome
 */
int is_palindrome(listint_t **head)
{
if (*head == NULL || (*head)->next == NULL)
return (1);

listint_t *slow = *head;
listint_t *fast = *head;
while (fast != NULL && fast->next != NULL)
{
slow = slow->next;
fast = fast->next->next;
}

listint_t *prev = NULL;
listint_t *curr = slow;
listint_t *next = NULL;
while (curr != NULL)
{
next = curr->next;
curr->next = prev;
prev = curr;
curr = next;
}

listint_t *first = *head;
listint_t *second = prev;
while (second != NULL)
{
if (first->n != second->n)
return (0);
first = first->next;
second = second->next;
}

return (1);
}
