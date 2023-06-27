#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - Prints basic info about Python lists.
 * @p: A PyObject list object.
 */
void print_python_list(PyObject *p)
{
  Py_ssize_t size, alloc, i;
  const char *type;

  if (!PyObject_TypeCheck(p, &PyList_Type))
    {
      printf("[ERROR] Invalid List Object\n");
      return;
    }

  size = ((PyVarObject *)p)->ob_size;
  alloc = ((PyListObject *)p)->allocated;

  printf("[*] Python list info\n");
  printf("[*] Size of the Python List = %ld\n", size);
  printf("[*] Allocated = %ld\n", alloc);

  for (i = 0; i < size; i++)
    {
      PyObject *item = ((PyListObject *)p)->ob_item[i];
      type = item->ob_type->tp_name;
      printf("Element %ld: %s\n", i, type);

      if (strcmp(type, "bytes") == 0)
	print_python_bytes(item);
      else if (strcmp(type, "float") == 0)
	print_python_float(item);
    }
}

/**
 * print_python_bytes - Prints basic info about Python byte objects.
 * @p: A PyObject byte object.
 */
void print_python_bytes(PyObject *p)
{
  Py_ssize_t size, i;
  char *str;

  if (!PyObject_TypeCheck(p, &PyBytes_Type))
    {
      printf("[ERROR] Invalid Bytes Object\n");
      return;
    }

  size = ((PyVarObject *)p)->ob_size;
  str = ((PyBytesObject *)p)->ob_sval;

  printf("[.] bytes object info\n");
  printf("  size: %ld\n", size);
  printf("  trying string: %s\n", str);
  printf("  first %ld bytes: ", size > 10 ? 10 : size);

  for (i = 0; i < size && i < 10; i++)
    printf("%02hhx%c", str[i], (i + 1 == size || i + 1 == 10) ? '\n' : ' ');
}

/**
 * print_python_float - Prints basic info about Python float objects.
 * @p: A PyObject float object.
 */
void print_python_float(PyObject *p)
{
  double value;

  if (!PyObject_TypeCheck(p, &PyFloat_Type))
    {
      printf("[ERROR] Invalid Float Object\n");
      return;
    }

  value = ((PyFloatObject *)p)->ob_fval;

  printf("[.] float object info\n");
  printf("  value: %f\n", value);
}
