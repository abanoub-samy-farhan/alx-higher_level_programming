#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *buffer = *head;
	listint_t *new = malloc(sizeof(listint_t));
	if (!new)
	{
		return (NULL);
	}

	new->n = number;

	while(buffer->next->n < number && buffer->next)
	{
		buffer = buffer->next;
	}

	new->next = buffer->next;
	buffer->next = new;

	return ((*head));
}
