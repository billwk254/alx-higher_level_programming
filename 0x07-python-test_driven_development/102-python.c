#include <Python.h>
#include <stdio.h>

/**
 * print_python_string - Prints information about a Python string object
 * @p: PyObject pointer to a Python object
 */
void print_python_string(PyObject *p)
{
	Py_ssize_t length;
	PyTypeObject *type;
	const char *value;

	printf("[.] string object info\n");

	if (!PyUnicode_Check(p))
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	type = Py_TYPE(p);
	length = PyUnicode_GET_LENGTH(p);
	value = PyUnicode_AsUTF8AndSize(p, &length);

	printf("  type: compact %s\n", type->tp_name);
	printf("  length: %ld\n", length);
	printf("  value: %s\n", value);
}
