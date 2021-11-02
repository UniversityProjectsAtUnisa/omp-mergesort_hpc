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

#include "merge_sort.h"

#include <omp.h>
#include <string.h>

void merge_sort(int *X, int n, int *tmp, int task_size) {
  if (n < 2) return;

#pragma omp task shared(X) if (n >= task_size)
  merge_sort(X, n / 2, tmp, task_size);

#pragma omp task shared(X) if (n >= task_size)
  merge_sort(X + n / 2, n - n / 2, tmp + n / 2, task_size);

#pragma omp taskwait
  merge(X, n / 2, X + n / 2, n - n / 2, tmp);
}

void merge(int *X, int n, int *Y, int m, int *tmp) {
  int i = 0, j = 0;

  while (i < n && j < m) {
    if (X[i] < Y[j]) {
      tmp[i + j] = X[i];
      i++;
    } else {
      tmp[i + j] = Y[j];
      j++;
    }
  }

  while (i < n) {
    tmp[i + j] = X[i];
    i++;
  }

  while (j < m) {
    tmp[i + j] = Y[j];
    j++;
  }
  memcpy(X, tmp, (i + j) * sizeof(int));
}