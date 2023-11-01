#include "lists.h"

/**
 * insert_node - add a new node to a sorted linked list
 * @head: a pointer to the head of the linked list
 * @number: the number to add to the sorted array
 *
 * Return: The pointer to the new node or NULL if fail
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp, *new_node;

	if (head == NULL)
		return (NULL);
	new_node = (listint_t *)malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	tmp = *head;
	if (number <= tmp->n || *head == NULL)
	{
		new_node->next = tmp;
		*head = new_node;
		return (new_node);
	}
	while (tmp->next != NULL)
	{
		if (number >= tmp->n && number <= (tmp->next)->n)
		{
			new_node->next = tmp->next;
			tmp->next = new_node;
			return (new_node);
		}
		tmp = tmp->next;
	}
	tmp->next = new_node;
	new_node->next = NULL;
	return (new_node);
}
