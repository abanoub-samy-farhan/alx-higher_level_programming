#include "lists.h"

int check_cycle(listint_t *list)
{
	if (list == NULL || list->next == NULL)
	{
		return 0;
	}
	listint_t *buffer = list;
	listint_t *fastbuffer = list;

	while (fastbuffer != NULL || fastbuffer->next != NULL)
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
