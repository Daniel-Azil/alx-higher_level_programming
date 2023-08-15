#include "lists.h"

/**
 * d_rvprototype - Initialised a function named d_rvprototype d_rvprototype list.
 * @1arg_1: Argument of the function d_rvprototype
 * Return: The function returns nothing.
 */
void d_rvprototype(listint_t **1arg_1)
{
	listint_t *prior_pnt1, *prsnt_pnt1, *cmng_pnt;
	prior_pnt1 = NULL;
	prsnt_pnt1 = *1arg_1;
	while (prsnt_pnt1 != NULL)
	{
		cmng_pnt = prsnt_pnt1->next;
		prsnt_pnt1->next = prior_pnt1;
		prior_pnt1 = prsnt_pnt1;
		prsnt_pnt1 = cmng_pnt;
	}

	*1arg_1 = prior_pnt1;
}

/**
 * az_prfunction - compares each int of the list
 * @2arg_t1: head of the first half
 * @2arg_t2: head of the second half
 * Return: 1 if are equals, 0 if not
 */
int az_prfunction(listint_t *2arg_t1, listint_t *2arg_t2)
{
	listint_t *ppnt2, *ppnt2_t;
	ppnt2 = 2arg_t1;
	ppnt2_t = 2arg_t2;
	while (ppnt2 != NULL && ppnt2_t != NULL)
	{
		if (ppnt2->n == ppnt2_t->n)
		{
			ppnt2 = ppnt2->next;
			ppnt2_t = ppnt2_t->next;
		}
		else
		{
			return (0);
		}
	}

	if (ppnt2 == NULL && ppnt2_t == NULL)
	{
		return (1);
	}

	return (0);
}

/**
 * is_palindrome - Inintialised a custom function of the
 * given name below.
 * @head: Argument to the initialised function.
 * Return: The function returns the value 0 or 1.
 */
int is_palindrome(listint_t **head)
{
	int variable_int;
	listint_t *var1_lt, *var2_lt, *var33_lt, *az_t, *da_pnt;
	var1_lt = var2_lt = var33_lt = *head;
	da_pnt = NULL;
	variable_int = 1;
	if (*head != NULL && (*head)->next != NULL)
	{
		while (var2_lt != NULL && var2_lt->next != NULL)
		{
			var2_lt = var2_lt->next->next;
			var33_lt = var1_lt;
			var1_lt = var1_lt->next;
		}
		if (var2_lt != NULL)
		{
			da_pnt = var1_lt;
			var1_lt = var1_lt->next;
		}
		az_t = var1_lt;
		var33_lt->next = NULL;
		d_rvprototype(&az_t);
		variable_int = az_prfunction(*head, az_t);
		if (da_pnt != NULL)
		{
			var33_lt->next = da_pnt;
			da_pnt->next = az_t;
		}
		else
		{
			var33_lt->next = az_t;
		}
	}
	return (variable_int);
}
