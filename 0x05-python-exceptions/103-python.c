#include <Python.h>
#include <stdio.h>

void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
* print_python_list - print info about the python
* Object
*
* @p: The python object
*/
void print_python_list(PyObject *p)
{
	Py_ssize_t size = 0, i, alloc;

	size = ((PyVarObject *)p)->ob_size;
	alloc = ((PyListObject *)p)->allocated;

	fflush(stdout);
	
	printf("[*] Python list info\n");
	if (strcmp(p->ob_type->tp_name, "list") != 0)
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
	printf("[*] Size of the Python List = %lu\n", size);
	printf("[*] Allocated = %lu\n", alloc);

	for (i = 0; i < size; i++)
	{
		printf("Element %ld: %s\n", i, ((PyListObject *)p)->ob_item[i]->ob_type->tp_name);
		if (strcmp(((PyListObject *)p)->ob_item[i]->ob_type->tp_name, "bytes") == 0)
			print_python_bytes(((PyListObject *)p)->ob_item[i]);
		if (strcmp(((PyListObject *)p)->ob_item[i]->ob_type->tp_name, "float") == 0)
			print_python_float(((PyListObject *)p)->ob_item[i]);
	}
}

/**
* print_python_bytes - Print info about the bytes content of a list
*
* @p: The item of type bytes
*
* Return: Anything, cause void function
*/
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	PyBytesObject *bytes = (PyBytesObject *)p;

	fflush(stdout);

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", bytes->ob_sval);

	if (((PyVarObject *)p)->ob_size >= 10)
		size = 10;
	else
		size = ((PyVarObject *)p)->ob_size + 1;

	printf("  first %ld bytes: ", size);
	for (i = 0; i < size; i++)
	{
		printf("%02hhx", bytes->ob_sval[i]);
		if (i == (size - 1))
			printf("\n");
		else
			printf(" ");
	}
}

/**
* print_python_float - Print info about the float content of a list
*
* @p: The item of type float
*
* Return: Anything, cause void function
*/
void print_python_float(PyObject *p)
{
	fflush(stdout);
	printf("[.] float object info\n");
	if (strcmp(p->ob_type->tp_name, "float") != 0)
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	printf("  value: %s\n", PyOS_double_to_string(((PyFloatObject *)p)->ob_fval,
	 	'r', 0, Py_DTSF_ADD_DOT_0, NULL));
}