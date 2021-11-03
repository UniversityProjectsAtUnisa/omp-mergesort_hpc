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
 * OMP Mergesort implementation is free software: you can redistribute it
 * and/or modify it under the terms of the GNU General Public License as
 * published by the Free Software Foundation, either version 3 of the License,
 * or (at your option) any later version.
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

/**
 * @file main.c
 * @brief measures the execution time of a parallel implementation of the merge_sort algorithm
 * 
 * @copyright Copyright (c) 2021
 * 
 */

#include "main.h"

#include <omp.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "merge_sort.h"

/**
 * @brief calls and measure the execution time of merge_sort function
 * 
 * @param argc numbers of arguments
 * @param argv arguments. Accept task_size as first argument. Defaults to 100.
 * @return int status code
 */
int main(int argc, char* argv[]) {
  DEBUG_PRINT("argc: %d\n", argc);
  int task_size = (argc > 1) ? atoi(argv[1]) : TASK_SIZE;
  DEBUG_PRINT("task_size: %d\n", task_size);
  size_t n;
  int *arr;
  read_file(&arr, &n);

  debug_print_array(arr, n);

  omp_set_dynamic(0);

  double end, start = omp_get_wtime();
#pragma omp parallel
  {
#pragma omp single
    merge_sort_tasksize(arr, n, task_size);
  }
  end = omp_get_wtime();
  printf("%f", end - start);
  debug_print_array(arr, n);

  free(arr);
  return EXIT_SUCCESS;
}

/**
 * @brief Allocates and populates and array with data in file FILENAME
 * 
 * @param arr 
 * @param n 
 */
void read_file(int** arr, size_t* n) {
  FILE* fp;
  if ((fp = fopen(FILENAME, "r")) == NULL) {
    DEBUG_PUTS("Input file not found");
    exit(EXIT_FAILURE);
  }

  fscanf(fp, "%ld\n", n);
  *arr = malloc(*n * sizeof(int));
  if (*arr == NULL) {
    DEBUG_PUTS("Memory could not be allocated");
    exit(EXIT_FAILURE);
  }

  DEBUG_PUTS("Reading from file...");
  for (size_t i = 0; i < *n; i++) {
    fscanf(fp, "%d", &(*arr)[i]);
  }
  fclose(fp);
}

void debug_print_array(int* arr, size_t size) {
  if (DEBUG) {
    for (size_t i = 0; i < size; i++) {
      printf("%d\n", arr[i]);
    }
  }
}
