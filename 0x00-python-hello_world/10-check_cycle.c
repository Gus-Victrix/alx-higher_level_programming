#include "lists.h"


/**
* find_listint_loop - Find if the list contain infinite loop
*
* @head: linked list
*
* Return: The numer of elem
*/
int check_cycle(listint_t *head)
{
	listint_t *tortoise;
	listint_t *hare;

	if (head == NULL || head->next == NULL)
		return (0);
	tortoise = hare = head;
	while (hare->next != NULL && hare->next->next != NULL)
	{
		tortoise = tortoise->next;
		hare = hare->next->next;
		if (tortoise == hare)
		{
            return(1);
		}
	}
	return(0);
}
