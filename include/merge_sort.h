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

#ifndef _MNT_C_USERS_MARCO_DOCUMENTS_UNISA_HPC_CODICE_CONTEST_OMP_INCLUDE_MERGE_SORT_H_
#define _MNT_C_USERS_MARCO_DOCUMENTS_UNISA_HPC_CODICE_CONTEST_OMP_INCLUDE_MERGE_SORT_H_

#define TASK_SIZE 100

#define merge_sort(X, n) merge_sort_tasksize(X, n, TASK_SIZE);

/**
 * @brief Merge sorts an array with parallel programming using a minimum task size
 * 
 * @param arr the array to be sorted
 * @param size the size of the array
 * @param task_size the minimum task size to create a new task
 */
void merge_sort_tasksize(int *arr, int size, int task_size);

/**
 * @brief Utility used by merge_sort_tasksize to implement the merge sort
 * 
 * @param arr the array to be sorted
 * @param size the size of the array
 * @param tmp the temporary array to implement the algorithm
 * @param task_size the minimum task size to create a new task
 */
void _merge_sort_aux(int *arr, int size, int *tmp, int task_size);

/**
 * @brief Utility used by _merge_sort_aux to implement the merging part in the merge sort
 * 
 * @param arr1 the first array to be merged
 * @param size1 the size of the first array
 * @param arr2 the second array to be merged
 * @param size2 the size of the second array
 * @param tmp the temporary array to implement the algorithm
 */
void _merge(int *arr1, int size1, int *arr2, int size2, int *tmp);

#endif  // _MNT_C_USERS_MARCO_DOCUMENTS_UNISA_HPC_CODICE_CONTEST_OMP_INCLUDE_MERGE_SORT_H_