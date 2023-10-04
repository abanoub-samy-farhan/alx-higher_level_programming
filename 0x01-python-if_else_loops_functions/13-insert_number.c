#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
	if (!(*head) || !(**head))
	{
		return (NULL);
	}
	listint_t *buffer = *head;
	listint_t *new = malloc(sizeof(listint_t));
	if (!new)
	{
		return (NULL);
	}

	new->n = number;
	if (buffer->n > new->n)
	{
		new->next = buffer;
		(*head) = new;
		return ((*head))
	}

	while(buffer->next != NULL)
	{
		if (buffer->next->n > new->n)
		{
			new->next = buffer->next;
			buffer->next = new;
			return ((*head));
		}
	}

	buffer->next = new;
	new->next = NULL;
	return ((*head));
}
