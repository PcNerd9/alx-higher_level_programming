#include "lists.h"


int check_cycle(listint_t *list)
{
        listint_t *hare, *tortise;

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
