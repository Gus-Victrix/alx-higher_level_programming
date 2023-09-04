#include <stdio.h>
#include <Python.h>

void print_python_string(PyObject *p)
{

    int size_str;

    printf("[.] string object info\n");
	if (strcmp(p->ob_type->tp_name, "str") != 0)
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

    if (PyUnicode_IS_COMPACT_ASCII(p))
        printf("  type: compact ascii\n");
    else
        printf("  type: compact unicode object\n");
    printf("  length: %ld\n", ((PyASCIIObject *)(p))->length);
    printf("  value: %ls\n", PyUnicode_AsWideCharString(p, NULL));
}