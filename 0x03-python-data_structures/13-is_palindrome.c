#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * is_palindrome - checks if a list is palindrome
 * @head: the head of the list
 *
 * Return: 1 if palindrome else return 0
 */
int is_palindrome(listint_t **head)
{
	int *number_int;
	listint_t *tmp;
	int i = 0, number_list = 0;

	if (head == NULL)
		return (-1);
	if (*head == NULL)
		return (1);
	tmp = *head;
	while (tmp != NULL)
	{
		number_list += 1;
		tmp = tmp->next;
	}
	if (number_list == 1)
		return (1);
	number_int = (int *)malloc(sizeof(int) * number_list);
	if (!number_int)
		return (-1);
	tmp = *head;
	while (tmp != NULL)
	{
		number_int[i++] = tmp->n;
		tmp = tmp->next;
	}
	for (i = 0; i < (number_list / 2); i++)
	{
		if (number_int[i] != number_int[number_list - 1 - i])
			return (0);
	}
	return (1);
}
