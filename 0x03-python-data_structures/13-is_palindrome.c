#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - function in C that checks if a singly linked list is a
 * palindrome
 * @head: Double pointer for linked dlistint_t list to head node
 * Return: 1 if palindrome, 0 if not
 */

int is_palindrome(listint_t **head)
{
	listint_t *median, *temp1, *temp2;
	int i, j, len = 0;

	if (*head == NULL || head == NULL)
		return (1);

	temp1 = *head;

	while (temp1 != NULL)
	{
		temp1 = temp1->next;
		++len;
	}

	if (len == 1)
		return (1);

	for (i = 0, temp1 = *head; i < len / 2 - 1; i++, temp1 = temp1->next)
	{
		temp2 = *head;
		j = 0;

		while (j < len - i - 1)
		{
			temp2 = temp2->next;
			j++;
		}

		if (temp1->n != temp2->n)
			return (0);

		if (len % 2 == 0)
			median = temp1->next;
	}
	if (median->n != temp1->n && median->n != temp2->n)
		return (1);

	return (1);
}
