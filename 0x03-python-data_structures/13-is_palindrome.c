#include<stddef.h>
#include "lists.h"
#include<stdio.h>
#include<stdlib.h>
int path_finder(listint_t *buffer1,int idx1, listint_t *buffer2,int idx2)
{
	while(idx1--)
	{
		buffer1 = buffer1->next;
	}
	while(idx2--)
	{
		buffer2 = buffer2->next;
	}

	if (buffer1->n == buffer2->n)
	{
		return 1;
	}
	else
	{
		return 0;
	}
}

int is_palindrome(listint_t **head)
{
	int len = 1, j = 0;
	int result;
	listint_t *buffer1 = *head, *buffer2 = *head;

	if (!(*head))
	{
		return 1;
	}

	while ((*head)->next != NULL)
	{
		len++;
		(*head) = (*head)->next;
	}
	for (; j < len; j++)
	{
		result = path_finder(buffer1, j, buffer2, len - j - 1);
		if (result == 0)
		{
			return 0;
		}
	}

	return 1;
}
