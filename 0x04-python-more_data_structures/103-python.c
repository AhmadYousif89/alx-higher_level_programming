#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - Print some basic info about Python bytes objects
 * @p: pointer to the PyObject
 */
void print_python_bytes(PyObject *p)
{
	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	Py_ssize_t size = PyBytes_Size(p);
	char *str = PyBytes_AsString(p);

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);

	printf("  first 10 bytes: ");
	for (Py_ssize_t i = 0; i < size && i < 10; ++i)
		printf("%02x ", (unsigned char)str[i]);

	printf("\n");
}

/**
 * print_python_list - print some basic info about Python lists
 * @p: pointer to the PyObject
 */
void print_python_list(PyObject *p)
{
	printf("[*] Python list info\n");

	if (!PyList_Check(p))
	{
		printf("[!] Invalid List Object\n");
		return;
	}

	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t allocated = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);

	for (Py_ssize_t i = 0; i < size; ++i)
	{
		printf("Element %ld: ", i);
		PyObject *elem = PyList_GetItem(p, i);

		if (PyBytes_Check(elem))
			print_python_bytes(elem);
		else if (PyLong_Check(elem))
			printf("int\n");
		else if (PyFloat_Check(elem))
			printf("float\n");
		else if (PyTuple_Check(elem))
			printf("tuple\n");
		else if (PyList_Check(elem))
			print_python_list(elem);
		else if (PyUnicode_Check(elem))
			printf("str\n");
		else
			printf("[!] Unknown type\n");
	}
}
