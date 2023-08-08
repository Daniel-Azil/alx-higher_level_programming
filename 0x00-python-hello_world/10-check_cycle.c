#include "lists.h"
/**
 * check_cycle - An initialised function with the name check_cycle.
 * @list: Struct list argument to the function check_cycle.
 * Return: The function returns 0 or 1.
 */

int check_cycle(listint_t *list)
{
	listint_t *struct_argument_node_1, *struct_argument_node_2;

	struct_argument_node_1 = list;
	struct_argument_node_2 = list;
	while (list && struct_argument_node_1 && struct_argument_node_1->next)
	{
		list = list->next;
		struct_argument_node_1 = struct_argument_node_1->next->next;

		if (list == struct_argument_node_1)
		{
			list = struct_argument_node_2;
			struct_argument_node_2 =  struct_argument_node_1;
			while (1)
			{
				struct_argument_node_1 = struct_argument_node_2;
				while (struct_argument_node_1->next != list && struct_argument_node_1->next != struct_argument_node_2)
				{
					struct_argument_node_1 = struct_argument_node_1->next;
				}
				if (struct_argument_node_1->next == list)
					break;

				list = list->next;
			}
			return (1);
		}
	}

	return (0);
}
