#include <Python.h>
#include <stdio.h>
#include <stdlib.h>

void print_python_list_info(PyObject *p)
{
    PyListObject *list = (PyListObject *)p;
    Py_ssize_t size = PyList_Size(p);
    Py_ssize_t i;
    PyListObject *listobj;

    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", list->allocated);

    for (i = 0; i < size; i++)
	{
        listobj = (PyListObject *)(list->ob_item[i]);
        printf("Element %ld: %s\n", i, Py_TYPE(list->ob_item[i])->tp_name);
    }
}
