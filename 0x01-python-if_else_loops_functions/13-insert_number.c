#include "lists.h"

/**
 * insert_node - Insert a number into a sorted singly-linked list.
 * @head: A pointer the head of the linked list.
 * @number: The number to insert.
 * Return: NULL on failuer otherwise the pointer to the new node.
 */
listint_t *insert_node(listint_t **head, int n)
{
	listint_t *current = *head;
	listint_t *new = malloc(sizeof(listint_t));

	if (!new || !head)
		return (NULL);

	new->n = n;
	new->next = NULL;

	if (!current || n <= current->n)
	{
		new->next = current;
		*head = new;
		return (new);
	}

	while (current->next && n > current->next->n)
		current = current->next;

	new->next = current->next;
	current->next = new;

	return (new);
}