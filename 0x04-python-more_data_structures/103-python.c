#include <Python.h>
#include <stdio.h>
#include <stdlib.h>

void print_python_list(PyObject *p) {
  Py_ssize_t size, i;
  PyObject *item;

  printf("[*] Python list info\n");

  if (!PyList_Check(p)) {
    printf("  [ERROR] Invalid List Object\n");
    return;
  }

  size = PyList_Size(p);
  printf("[*] Size of the Python List = %ld\n", size);
  printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

  for (i = 0; i < size; i++) {
    item = PyList_GetItem(p, i);
    printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
  }
}

void print_python_bytes(PyObject *p) {
  Py_ssize_t size, i;
  char *str;

  printf("[.] bytes object info\n");

  if (!PyBytes_Check(p)) {
    printf("  [ERROR] Invalid Bytes Object\n");
    return;
  }

  size = PyBytes_Size(p);
  str = PyBytes_AsString(p);

  printf("  size: %ld\n", size);
  printf("  trying string: %s\n", str);

  printf("  first %ld bytes: ", size + 1);
  if (size >= 10)
    size = 10;
  for (i = 0; i <= size; i++) {
    printf("%02x", (unsigned char)str[i]);
    if (i == size)
      break;
    printf(" ");
  }
  printf("\n");
}
