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
 *
 * You should have received a copy of the GNU General Public License
 * along with OMP Mergesort implementation.  If not, see <http:
 * //www.gnu.org/licenses/>.
 */

/**
 * @file merge_sort.c
 * @brief implements a parallel version of the merge_sort algorithm
 * 
 * @copyright Copyright (c) 2021
 * 
 */

#include "merge_sort.h"

#include <omp.h>
#include <stdlib.h>
#include <string.h>


/**
 * @brief Merge sorts an array with parallel programming using a minimum task size
 * 
 * @param arr the array to be sorted
 * @param size the size of the array
 * @param task_size the minimum task size to create a new task
 */
void merge_sort_tasksize(int *arr, int size, int task_size) {
  if (size < 0) return;
  int *tmp = malloc(size * sizeof(int));
  _merge_sort_aux(arr, size, tmp, task_size);
  free(tmp);
}


/**
 * @brief Utility used by merge_sort_tasksize to implement the merge sort
 * 
 * @param arr the array to be sorted
 * @param size the size of the array
 * @param tmp the temporary array to implement the algorithm
 * @param task_size the minimum task size to create a new task
 */
void _merge_sort_aux(int *arr, int size, int *tmp, int task_size) {
  if (size < 2) return;

#pragma omp task shared(arr) if (size >= task_size)
  _merge_sort_aux(arr, size / 2, tmp, task_size);

#pragma omp task shared(arr) if (size >= task_size)
  _merge_sort_aux(arr + size / 2, size - size / 2, tmp + size / 2, task_size);

#pragma omp taskwait
  _merge(arr, size / 2, arr + size / 2, size - size / 2, tmp);
}


/**
 * @brief Utility used by _merge_sort_aux to implement the merging part in the merge sort
 * 
 * @param arr1 the first array to be merged
 * @param size1 the size of the first array
 * @param arr2 the second array to be merged
 * @param size2 the size of the second array
 * @param tmp the temporary array to implement the algorithm
 */
void _merge(int *arr1, int size1, int *arr2, int size2, int *tmp) {
  int i = 0, j = 0;

  while (i < size1 && j < size2) {
    if (arr1[i] < arr2[j]) {
      tmp[i + j] = arr1[i];
      i++;
    } else {
      tmp[i + j] = arr2[j];
      j++;
    }
  }

  while (i < size1) {
    tmp[i + j] = arr1[i];
    i++;
  }

  while (j < size2) {
    tmp[i + j] = arr2[j];
    j++;
  }
  memcpy(arr1, tmp, (i + j) * sizeof(int));
}