#include "Python.h"

/**
 * print_python_sting - Print info about python strings
 * @p: A PyObject string object
 */
void print_python_string(PyObject *p)
{
	fflush(stdout);

	printf("[.] string object info\n");
	if (strcmp(p->ob_type->tp_name, "str"))
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");

	printf("  length: %lu\n", PyUnicode_GET_LENGTH(p));
	printf("  value: %ls\n",
		   PyUnicode_AsWideCharString(p, &((PyASCIIObject *)(p))->length));
}
