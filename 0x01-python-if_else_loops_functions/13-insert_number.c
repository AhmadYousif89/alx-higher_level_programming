#include "lists.h"

listint_t *insert_node(listint_t **head, int n)
{
	unsigned int i = 0;
	listint_t *cur_node = *head;
	listint_t *new_node = malloc(sizeof(listint_t));

	if (!new_node || !head)
		return (NULL);

	new_node->n = n;

	while (cur_node)
	{
		if (cur_node->n > n)
		{
			new_node->next = cur_node->next;
			cur_node->next = new_node;
			return (new_node);
		}
		cur_node = cur_node->next;
		i++;
	}

	return (NULL);
}