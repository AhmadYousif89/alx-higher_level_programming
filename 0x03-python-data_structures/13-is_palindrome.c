#include "lists.h"

/**
 * _helper - .
 * @start: pointer to the head of the list
 * @end: pointer to the head of the list
 * Return: 1 or 0
 */
int _helper(listint_t **start, listint_t *end)
{
	int result = 0;

	if (end == NULL) /* End of the list, reached without finding a mismatch */
		return (1);	 /* A palindrome */

	result = _helper(start, end->next);
	if (!result || (*start)->n != end->n)
		return (0); /* Not a palindrome */

	*start = (*start)->next; /* Move to the next node */
	return (1);
}

/**
 * is_palindrome - Check for palindrome in singly linked lists
 * @head: pointer to the list
 * Return: 1 if palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp = *head;

	if (!head || !*head) /* Empty lists */
		return (1);		 /* A palindrome */

	return (_helper(head, temp));
}
