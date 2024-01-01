#include "lists.h"

/**
 * check_cycle - Check for loop inside a singly linked list
 * @list: pointer to the head of the list
 * Return: 1 if cycle found, 0 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *hare = list, *tortoise = list;

	if (!list)
		return (0);

	while (tortoise && hare && hare->next)
	{
		hare = hare->next->next;
		tortoise = tortoise->next;

		if (tortoise == hare)
		{
			tortoise = list;
			while (tortoise != hare)
			{
				tortoise = tortoise->next;
				hare = hare->next;
			}
			return (1);
		}
	}

	return (0);
}
