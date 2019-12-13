#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - function that inserts a number into a sorted singly linked
 * list
 * @head: double pointer for linked list nodes
 * @number: integer to be inserted
 * Return: address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	int curr_num, next_num;
	listint_t *new, *current, *temp;

	current = *head;
	new = malloc(sizeof(listint_t));

	if (new == NULL)
		return (NULL);

	if (*head == NULL || (*head)->n >= number)
	{
		new->next = *head;
		new->n = number;
		*head = new;
		return (*head);
	}
	while (current->next != NULL)
	{
		curr_num = current->n;
		temp = current->next;
		next_num = temp->n;
		if (number > curr_num && number <= next_num)
		{
			new->n = number;
			new->next = current->next;
			current->next = new;
			return (new);
		}
		current = current->next;
		if (current->next == NULL)
		{
			new->n = number;
			new->next = current->next;
			current->next = new;
			return (new);
		}
	}
	return (NULL);
}
