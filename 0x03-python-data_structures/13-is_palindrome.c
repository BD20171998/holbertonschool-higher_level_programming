#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * len - function that returns number of nodes of a linked list
 * @alist: pointer of linked list listint_t
 * Return: number of nodes
 */

int len(listint_t *alist)
{
	listint_t *temp1;
	int len = 0;

	temp1 = alist;

	while (temp1 != NULL)
	{
		temp1 = temp1->next;
		++len;
	}
	return (len);
}

/**
 * reverse_listint - function that reverses a listint_t linked list
 * @head: Double pointer of linked list listint_t
 * @temp1: Double pointer of linked list listint_t -2nd copy
 * Return: Pointer to the middle node of the reversed list
 */

listint_t *reverse_listint(listint_t **head, listint_t **temp1)
{
	listint_t *prev;
	listint_t *future;

	int i = 0, l;

	l = len(*head);

	prev = NULL;

	while (i < l / 2)
	{
		future = (*head)->next;
		(*head)->next = prev;
		prev = *head;
		*head = future;
		++i;
	}

	*head = prev;

	if (l % 2 != 0)
		*temp1 = future->next;

	else
		*temp1 = future;

	return (*head);
}

/**
 * is_palindrome - function in C that checks if a singly linked list is a
 * palindrome
 * @head: Double pointer for linked dlistint_t list to head node
 * Return: 1 if palindrome, 0 if not
 */

int is_palindrome(listint_t **head)
{

	listint_t *temp1;
	listint_t *temp2;

	int i = 0, l;

	if (*head == NULL || head == NULL)
		return (1);

	l  = len(*head);

	if (l == 1)
		return (1);

	temp1 = *head;
	temp2 = reverse_listint(head, &temp1);

	while (i < (l / 2))
	{
		if (temp1->n != temp2->n)
			return (0);

		temp1 = temp1->next;
		temp2 = temp2->next;

		++i;
	}

	return (1);
}
