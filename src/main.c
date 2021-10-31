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
 * Copyright (C) 2021 Alessandro De Stefano (EarendilTiwele) Marco Della Rocca (marco741)
 * 
 * This file is part of OMP Mergesort implementation.
 * 
 * OMP Mergesort implementation is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 * 
 * OMP Mergesort implementation is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with OMP Mergesort implementation.  If not, see <http: //www.gnu.org/licenses/>.
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <omp.h>
#include "merge_sort.h"
#include "main.h"

int main(int argc, char *argv[])
{
    dprintf("argc: %d\n", argc);
    int task_size = (argc > 1) ? atoi(argv[1]) : 100;
    dprintf("task_size: %d\n", task_size);
    int n;
    int *arr, *temp;
    read_file(&arr, &n);
    temp = malloc(n * sizeof(int));

    for (size_t i = 0; i < n; i++)
    {
        dprintf("%d\n", arr[i]);
    }

    double end, start = omp_get_wtime();
#pragma omp parallel
    {
#pragma omp single
        merge_sort(arr, n, temp, task_size);
    }
    end = omp_get_wtime();
    printf("%f", end - start);
    for (size_t i = 0; i < n; i++)
    {
        dprintf("%d\n", arr[i]);
    }

    free(arr);
    free(temp);
    return EXIT_SUCCESS;
}

void read_file(int **arr, int *n)
{
    FILE *fp;
    if ((fp = fopen(FILENAME, "r")) == NULL)
    {
        dputs("Input file not found");
        exit(EXIT_FAILURE);
    }

    fscanf(fp, "%d\n", n);
    *arr = malloc(*n * sizeof(int));
    if (*arr == NULL)
    {
        dputs("Memory could not be allocated");
        exit(EXIT_FAILURE);
    }

    dputs("Reading from file...");
    for (size_t i = 0; i < *n; i++)
    {
        fscanf(fp, "%d", &(*arr)[i]);
    }
    fclose(fp);
}