#include <Python.h>

/**
 * print_python_bytes - Print some basic info about Python bytes objects
 * @p: pointer to the PyObject
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t i, size, limit;
	char *str;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	str = ((PyBytesObject *)p)->ob_sval;
	size = ((PyVarObject *)(p))->ob_size;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);

	limit = size > 10 ? 10 : size + 1;

	printf("  first %ld bytes: ", limit);
	for (i = 0; i < size && i < limit; ++i)
		printf("%02x ", (unsigned char)str[i]);
	printf("\n");
}

/**
 * print_python_list - print some basic info about Python lists
 * @p: pointer to the PyObject
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t i, size, allocated;

	size = ((PyVarObject *)p)->ob_size;
	allocated = ((PyListObject *)p)->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);

	for (i = 0; i < size; ++i)
	{
		PyObject *item = ((PyListObject *)p)->ob_item[i];

		printf("Element %ld: %s\n", i, ((item)->ob_type)->tp_name);
		if (PyBytes_Check(item))
			print_python_bytes(item);
	}
}
