#ifndef LIST_H
#define LIST_H

#include <stddef.h>
#include <unistd.h>
#include <stdlib.h>

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 *
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

int check_cycle(listint_t *list);
void *_realloc(void *,int , int);
void *_memcpy(void *,const void *, int);

#endif
