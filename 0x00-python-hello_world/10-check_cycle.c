#include "lists.h"

/**
 * check_cycle - check if a cycle is present in linked
 * list
 * @list: the head to the linked list
 * Return: 0 if not present otherwise return 1
 */
int check_cycle(listint_t *list)
{
	listint_t *hare, *tortise;

	if (list == NULL)
		return (0);
	hare = list;
	tortise = list;
	while (hare)
	{
		hare = (hare->next)->next;
		tortise = tortise->next;
		if (hare == tortise)
			return (1);
	}
	return (0);
}
