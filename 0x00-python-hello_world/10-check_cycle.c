#include "lists.h"

/**
 * check_cycle - checks for cycles in singly linked lists.
 *
 * @list: pointer to the head of the list.
 *
 * Return: 0 if none found, 1 if there is a cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *current = list;
	listint_t **arr = 0;
	short n = 0;
	short size = 0;
	short i = 0;

	if (list == NULL)
		return (0);
	
	while (current != NULL)
	{
		if (n == size)
		{
			size += 10;
			arr = _realloc(arr, size * sizeof(listint_t **), (size - 10) *
					sizeof(listint_t **));
		}
		while (i < n)
		{
			if (arr[i++] == current)
			{
				free(arr);
				return (1);
			}
		}
		arr[i] = current;
		current = current->next;
	}
	return (0);
}

/**
 * _realloc - Reallocates Memory
 *
 * @ptr: Pointer to memory block that's to be reallocated.
 * @size: New size of allocated memory.
 * @old_size: Current size of malloc block.
 *
 * Return: Pointer to new memory block.
 */
void *_realloc(void* ptr, int size, int old_size)
{
	void *new_ptr = NULL;

    if (size == 0)
	{
        free(ptr);
        return (NULL);
    }

    if (ptr == NULL)
	{
        return (malloc(size));
    }

    new_ptr = malloc(size);
    if (new_ptr == NULL)
	{
        return (NULL); 
    }

    _memcpy(new_ptr, ptr, ((old_size < size) ? old_size : size) *
			sizeof(listint_t **));

    free(ptr);
    return (new_ptr);
}

/**
 * _memcpy - copies memery content from one to the other
 *
 * @dest: Destination memeory.
 * @src: source of memery
 * @n: Size of memory block
 *
 * Return: destination address.
 */
void* _memcpy(void* dest, const void* src, int n)
{
    unsigned char* dest_ptr = (unsigned char*)dest;
    const unsigned char* src_ptr = (const unsigned char*)src;
	int i = 0;

    for (i = 0; i < n; i++)
	{
        dest_ptr[i] = src_ptr[i];
    }

    return (dest);
}

