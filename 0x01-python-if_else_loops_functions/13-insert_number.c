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
	if (!(*head))
	{
		new->next = NULL;
		(*head) = new;
		return (new);
	}
	if (buffer->n > new->n)
	{
		new->next = buffer;
		(*head) = new;
		return (new);
	}

	while(buffer->next)
	{
		if (buffer->next->n > new->n)
		{
			new->next = buffer->next;
			buffer->next = new;
			return ((*head));
		}
		buffer = buffer->next;
	}
	buffer->next = new;
	new->next = NULL;
	return ((*head));
}
