#include "lists.h"

/**
* check_cycle - Checks if a list node has a cycle
* @list: A list node
* Return: 0 for no cycle and 1 for cycle found
*/
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (list == NULL || list->next == NULL)
	{
		return (0);
	}

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
		{
			return (1);
		}
	}

	return (0);
}

