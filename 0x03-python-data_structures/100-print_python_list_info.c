#include <Python.h>
#include <stdio.h>
#include <object.h>
#include <listobject.h>

/**
* print_python_list_info - Function that print some basic info
* about Python lists
* @p: object Pointer
* Return: void
*/
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, allocated, i;
	PyObject *item;

	size = PyList_Size(p);
	allocated = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		print("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}

