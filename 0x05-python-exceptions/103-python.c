#include <Python.h>
#include <stdio.h>
#include <stdlib.h>

/**
 * print_python_list - Prints information about a Python list object
 * @p: PyObject pointer to the Python list
 */
void print_python_list(PyObject *p)
{
Py_ssize_t size, i;
PyObject *item;

printf("[*] Python list info\n");
printf("[*] Size of the Python List = %ld\n", Py_SIZE(p));
printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

size = Py_SIZE(p);
for (i = 0; i < size; i++)
{
item = PyList_GetItem(p, i);
printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
}
}

/**
 * print_python_bytes - Prints information about a Python bytes object
 * @p: PyObject pointer to the Python bytes object
 */
void print_python_bytes(PyObject *p)
{
Py_ssize_t size, i;
char *str;

printf("[.] bytes object info\n");
if (!PyBytes_Check(p))
{
printf("  [ERROR] Invalid Bytes Object\n");
return;
}

size = PyBytes_Size(p);
str = PyBytes_AsString(p);

printf("  size: %ld\n", size);
printf("  trying string: %s\n", str);

printf("  first %ld bytes: ", size + 1 > 10 ? 10 : size + 1);
for (i = 0; i < size + 1 && i < 10; i++)
printf("%02x%c", (unsigned char)str[i], i + 1 < size + 1 && i + 1 < 10 ? ' ' : '\n');
}

/**
 * print_python_float - Prints information about a Python float object
 * @p: PyObject pointer to the Python float object
 */
void print_python_float(PyObject *p)
{
PyObject *repr;

printf("[.] float object info\n");
if (!PyFloat_Check(p))
{
printf("  [ERROR] Invalid Float Object\n");
return;
}

repr = PyObject_Repr(p);
if (repr)
{
printf("  value: %s\n", PyUnicode_AsUTF8(repr));
Py_DECREF(repr);
}
else
{
printf("  [ERROR] Failed to get float representation\n");
}
}
