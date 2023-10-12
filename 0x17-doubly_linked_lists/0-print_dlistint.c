#include "lists.h"

/**
 *
 *
 *
 *
 *
 *
 */

size_t print_dlistint(const dlistint_t *h)
{
	int count = 0;

	if (!h)
	{
		return count;
	}

	while (h)
	{
		count++;
		printf("%d\n", h->n);
		h = h->next;
	}

	return count;
}
