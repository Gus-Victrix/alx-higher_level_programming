#include "lists.h"

int compare_lists(listint_t *list1, listint_t *list2);
void reverse_list(listint_t **head);
/**
 * is_palindrome - Checks if a list is a palindrome
 *
 * @head: Head of the list to be checked
 *
 * Return: 1 if input is a palindrome, 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
    listint_t *slow = *head, *fast = *head;
    listint_t *prev_slow = *head, *second_half, *mid_node = NULL;
    int result = 1;

    if (*head != NULL && (*head)->next != NULL)
    {
        while (fast != NULL && fast->next != NULL)
        {
            fast = fast->next->next;

            prev_slow = slow;
            slow = slow->next;
        }

        if (fast != NULL)
        {
            mid_node = slow;
            slow = slow->next;
        }

        second_half = slow;
        prev_slow->next = NULL;
        reverse_list(&second_half);

        result = compare_lists(*head, second_half);

        reverse_list(&second_half);

        if (mid_node != NULL)
        {
            prev_slow->next = mid_node;
            mid_node->next = second_half;
        }
        else
        {
            prev_slow->next = second_half;
        }
    }

    return (result);
}

/**
 * reverse_list - Reverses the input list
 *
 * @head: Head of the input list
 */
void reverse_list(listint_t **head)
{
    listint_t *prev = NULL;
    listint_t *current = *head;
    listint_t *next;

    while (current != NULL)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }

    *head = prev;
}

/**
 * compare_lists - Compares two lists
 *
 * @list1: First of the lists being compared
 * @list2: Second of the lists being compared
 *
 * Return: 1 if the lists are similar, 0 otherwise.
 */
int compare_lists(listint_t *list1, listint_t *list2)
{
    while (list1 != NULL && list2 != NULL)
    {
        if (list1->n != list2->n)
            return (0);
        list1 = list1->next;
        list2 = list2->next;
    }

    if (list1 == NULL && list2 == NULL)
        return (1);
    return (0);
}
