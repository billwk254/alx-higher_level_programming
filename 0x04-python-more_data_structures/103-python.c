#include <stdio.h>
#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_list - Prints list information
 *
 * @p: Python Object
 * Return: no return
 */
void print_python_list(PyObject *p)
{
  PyListObject *list = (PyListObject *)p;
  long int size, i;

  size = _PyList_Size(p);

  printf("[*] Python list info\n");
  printf("[*] Size of the Python List = %ld\n", size);
  printf("[*] Allocated = %ld\n", list->allocated);

  for (i = 0; i < size; i++)
    {
      PyObject *obj = list->ob_item[i];
      const char *type_name = Py_TYPE(obj)->tp_name;

      printf("Element %ld: %s\n", i, type_name);
    }
}

/**
 * print_python_bytes - Prints bytes information
 *
 * @p: Python Object
 * Return: no return
 */
void print_python_bytes(PyObject *p)
{
  PyBytesObject *bytes = (PyBytesObject *)p;
  long int size, i, limit;

  printf("[.] bytes object info\n");

  if (!PyBytes_Check(p))
    {
      printf("  [ERROR] Invalid Bytes Object\n");
      return;
    }

  size = PyBytes_GET_SIZE(p);
  limit = size > 10 ? 10 : size;

  printf("  size: %ld\n", size);
  printf("  trying string: %s\n", bytes->ob_sval);
  printf("  first %ld bytes:", limit);

  for (i = 0; i < limit; i++)
    printf(" %02x", (unsigned char)bytes->ob_sval[i]);

  printf("\n");
}
