#include "lists.h"

/**
 * check_cycle - function to check cyclic linked lists
 * @list: list
 * Return: 1 or 0 on sucess
 *
 *
 */

int check_cycle(listint_t *list)
{
	if (list == NULL || list->next == NULL)
		return 0;

	listint_t *buffer = list;
	listint_t *fastbuffer = list;

	while (fastbuffer && fastbuffer->next)
	{
		buffer = buffer->next;
		fastbuffer = fastbuffer->next->next;

		if (buffer == fastbuffer)
		{
			return 1;
		}
	}

	return 0;
}
