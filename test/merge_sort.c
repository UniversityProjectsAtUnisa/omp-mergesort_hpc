/*
 * Course: High Performance Computing 2020/2021
 *
 * Lecturer: Francesco Moscato    fmoscato@unisa.it
 *
 * Group:
 * De Stefano Alessandro   0622701470  a.destefano56@studenti.unisa.it
 * Della Rocca Marco   0622701573  m.dellarocca22@studenti.unisa.it
 *
 * OMP implementation of mergesort algorithm
 * Copyright (C) 2021 Alessandro De Stefano (EarendilTiwele) Marco Della Rocca
 * (marco741)
 *
 * This file is part of OMP Mergesort implementation.
 *
 * OMP Mergesort implementation is free software: you can redistribute it and/or
 * modify it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * OMP Mergesort implementation is distributed in the hope that it will be
 * useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with OMP Mergesort implementation.  If not, see <http:
 * //www.gnu.org/licenses/>.
 */

#include "merge_sort.h"

#include <assert.h>
#include <stdlib.h>

int _is_sorted(int *a, int size) {
  for (int i = 0; i < size - 1; i++)
    if (a[i] > a[i + 1]) return 0;
  return 1;
}

void _load_from_stackarr(int *heap_array, int *stack_array, int size) {
  for (size_t i = 0; i < size; i++) heap_array[i] = stack_array[i];
}

int _equals_with_stackarr(int *heap_array, int *stack_array, int size) {
  for (size_t i = 0; i < size; i++)
    if (heap_array[i] != stack_array[i]) return 0;
  return 1;
}

void _test_merge_sort(int *stack_arr, int *solution, int size) {
  int *arr = malloc(size * sizeof(int));
  _load_from_stackarr(arr, stack_arr, size);

  merge_sort(arr, size);
  assert(_equals_with_stackarr(arr, solution, size) == 1);
  assert(_is_sorted(arr, size) == 1);
}

void _test_merge_sort_tasksize(int *stack_arr, int *solution, int size,
                               int task_size) {
  int *arr = malloc(size * sizeof(int));
  _load_from_stackarr(arr, stack_arr, size);

  merge_sort_tasksize(arr, size, task_size);
  assert(_equals_with_stackarr(arr, solution, size) == 1);
  assert(_is_sorted(arr, size) == 1);
}

void test_empty_array() {
  int size = 0;
  int stack_arr[0] = {};
  int solution[0] = {};

  _test_merge_sort(stack_arr, solution, size);
}

void test_one_element() {
  int size = 1;
  int stack_arr[1] = {1};
  int solution[1] = {1};

  _test_merge_sort(stack_arr, solution, size);
}

void test_descendent() {
  int size = 5;
  int stack_arr[5] = {5, 2, -1, -4, -6};
  int solution[5] = {-6, -4, -1, 2, 5};

  _test_merge_sort(stack_arr, solution, size);
}

void test_full_different() {
  int size = 5;
  int stack_arr[5] = {5, -1, 4, 2, -6};
  int solution[5] = {-6, -1, 2, 4, 5};

  _test_merge_sort(stack_arr, solution, size);
}

void test_full_equals() {
  int size = 5;
  int stack_arr[5] = {42, 42, 42, 42, 42};
  int solution[5] = {42, 42, 42, 42, 42};

  _test_merge_sort(stack_arr, solution, size);
}

void test_some_equals() {
  int size = 5;
  int stack_arr[5] = {5, -1, 5, 2, 6};
  int solution[5] = {-1, 2, 5, 5, 6};

  _test_merge_sort(stack_arr, solution, size);
}

void test_full_positive() {
  int size = 5;
  int stack_arr[5] = {5, 1, 4, 2, 6};
  int solution[5] = {1, 2, 4, 5, 6};

  _test_merge_sort(stack_arr, solution, size);
}

void test_full_negative() {
  int size = 5;
  int stack_arr[5] = {-5, -1, -4, -2, -6};
  int solution[5] = {-6, -5, -4, -2, -1};

  _test_merge_sort(stack_arr, solution, size);
}

void test_ordered() {
  int size = 5;
  int stack_arr[5] = {-3, -2, 1, 5, 6};
  int solution[5] = {-3, -2, 1, 5, 6};

  _test_merge_sort(stack_arr, solution, size);
}

void test_fail_n() {
  int size = 5;
  int stack_arr[5] = {-3, -2, 1, 5, 6};

  int *arr = malloc(size * sizeof(int));
  _load_from_stackarr(arr, stack_arr, size);

  merge_sort(arr, -2);
  assert(_equals_with_stackarr(arr, stack_arr, size) == 1);
}

void test_explicit_tasksize() {
  int size = 5;
  int stack_arr[5] = {5, -1, 4, 2, -6};
  int solution[5] = {-6, -1, 2, 4, 5};
  int task_size = 200;

  _test_merge_sort_tasksize(stack_arr, solution, size, task_size);
}

int main(int argc, char const *argv[]) {
  test_empty_array();
  test_one_element();
  test_descendent();
  test_full_different();
  test_full_equals();
  test_some_equals();
  test_full_positive();
  test_full_negative();
  test_ordered();
  test_fail_n();
  test_explicit_tasksize();
  return 0;
}