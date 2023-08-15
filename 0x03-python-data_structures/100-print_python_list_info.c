#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - Initialised a function
 * named print_python_list_info
 * @p: Argument of the initialised function.
 * Return: The function returns nothing.
 */
void print_python_list_info(PyObject *p)
{
	long int int_variable;
	long int d_n1;
	PyObject *pnt;
	PyListObject *pnt2;
	d_n1 = Py_SIZE(p);
	printf("[*] Size of the Python List = %ld\n", d_n1);

	pnt2 = (PyListObject *)p;
	printf("[*] Allocated = %ld\n", pnt2->allocated);

	for (int_variable = 0; int_variable < d_n1; int_variable++)
	{
		pnt = PyList_GetItem(p, int_variable);
		printf("Element %ld: %s\n", int_variable, Py_TYPE(pnt)->tp_name);
	}
}
