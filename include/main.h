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
#ifndef _MNT_C_USERS_MARCO_DOCUMENTS_UNISA_HPC_CODICE_CONTEST_OMP_INCLUDE_MAIN_H_
#define _MNT_C_USERS_MARCO_DOCUMENTS_UNISA_HPC_CODICE_CONTEST_OMP_INCLUDE_MAIN_H_

#include <time.h>

#define DEBUG 0
#define FILENAME "input/in.txt"

#define STARTTIME(id)                           \
  clock_t start_time_42_##id, end_time_42_##id; \
  start_time_42_##id = clock()

#define ENDTIME(id, x)        \
  end_time_42_##id = clock(); \
  x = ((double)(end_time_42_##id - start_time_42_##id)) / CLOCKS_PER_SEC

#define DEBUG_PUTS \
  if (DEBUG) puts

#define DEBUG_PRINT \
  if (DEBUG) printf

void read_file(int **arr, size_t *n);
void debug_print_array(int *arr, size_t n);

#endif  // _MNT_C_USERS_MARCO_DOCUMENTS_UNISA_HPC_CODICE_CONTEST_OMP_INCLUDE_MAIN_H_
