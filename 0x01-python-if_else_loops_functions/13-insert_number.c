#include "lists.h"
/**
 * insert_node - Initialised function named insert_node.
 * @head: Argument of the initialised function.
 * @number: Argument of the initialised function.
 * Return: Returns NULL or new node as specified in the task.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *updatedVar_t, *az_inceptionVar_t, *priorValue_t;

	az_inceptionVar_t = *head;

	updatedVar_t = malloc(sizeof(listint_t));

	if (updatedVar_t == NULL)
		return (NULL);
	while (az_inceptionVar_t != NULL)
	{
		if (az_inceptionVar_t->n > number)
			break;
		priorValue_t = az_inceptionVar_t;
		az_inceptionVar_t = az_inceptionVar_t->next;
	}
	updatedVar_t->n = number;
	if (*head == NULL)
	{
		updatedVar_t->next = NULL;
		*head = updatedVar_t;
	}
	else
	{
		updatedVar_t->next = az_inceptionVar_t;
		if (az_inceptionVar_t == *head)
			*head = updatedVar_t;
		else
			priorValue_t->next = updatedVar_t;
	}
	return (updatedVar_t);
}
