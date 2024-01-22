#include <Python.h>

/**
 * print_python_float - Print some basic info about Python float objects
 * @p: pointer to the PyObject
 */
void print_python_float(PyObject *p)
{
	double f;

	setbuf(stdout, NULL);
	printf("[.] float object info\n");
	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	f = ((PyFloatObject *)p)->ob_fval;
	printf("  value: %s\n",
		   PyOS_double_to_string(f, 'r', 0, Py_DTSF_ADD_DOT_0, NULL));
}

/**
 * print_python_bytes - Print some basic info about Python bytes objects
 * @p: pointer to the PyObject
 */
void print_python_bytes(PyObject *p)
{
	char *str;
	Py_ssize_t i, size, limit;

	setbuf(stdout, NULL);
	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	str = ((PyBytesObject *)p)->ob_sval;
	size = ((PyVarObject *)p)->ob_size;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);

	limit = size >= 10 ? 10 : size + 1;

	printf("  first %ld bytes:", limit);

	for (i = 0; i < limit; i++)
		printf(" %02x", (unsigned char)str[i]);

	printf("\n");
}

/**
 * print_python_list - print some basic info about Python lists
 * @p: pointer to the PyObject
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, i, allocated;
	PyObject *obj;

	setbuf(stdout, NULL);
	size = ((PyVarObject *)p)->ob_size;
	allocated = ((PyListObject *)p)->allocated;

	printf("[*] Python list info\n");

	if (PyList_CheckExact(p))
	{
		printf("[*] Size of the Python List = %ld\n", size);
		printf("[*] Allocated = %ld\n", allocated);
		for (i = 0; i < size; i++)
		{
			obj = ((PyListObject *)p)->ob_item[i];
			printf("Element %ld: %s\n", i, ((obj)->ob_type)->tp_name);
			if (PyBytes_Check(obj))
				print_python_bytes(obj);
			else if (PyFloat_Check(obj))
				print_python_float(obj);
		}
	}
	else
		printf("  [ERROR] Invalid List Object\n");
}
