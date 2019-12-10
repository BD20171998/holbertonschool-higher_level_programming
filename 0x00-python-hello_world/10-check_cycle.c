#include "lists.h"

/**
 * check_cycle - function that checks if a singly linked list has a
 * cycle in it
 * @list: pointer to the head of a listint_t list
 * Return: 1 if linked list has a cycle, 0 if not
 */

int check_cycle(listint_t *list)
{
	listint_t *current;

	current = list;

	while (current != NULL)
	{
		if (current->next == list)
			return (1);

		current = current->next;
	}

	return (0);
}
