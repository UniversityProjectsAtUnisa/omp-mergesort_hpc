'''
Course: High Performance Computing 2020/2021

Lecturer: Francesco Moscato    fmoscato@unisa.it

Group: 
De Stefano Alessandro   0622701470  a.destefano56@studenti.unisa.it
Della Rocca Marco   0622701573  m.dellarocca22@studenti.unisa.it

OMP implementation of mergesort algorithm 
Copyright (C) 2021 Alessandro De Stefano (EarendilTiwele) Marco Della Rocca (marco741)

This file is part of OMP Mergesort implementation.

OMP Mergesort implementation is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

OMP Mergesort implementation is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with OMP Mergesort implementation.  If not, see <http: //www.gnu.org/licenses/>.
'''

import subprocess
from generate_file import generate_file


def run_command(command):
    commands = ["bash", "-c", command]
    return subprocess.run(commands, capture_output=True)


def make_measures(num_threads, O_level, task_size, repetitions, execution="parallel"):
    total_time = 0
    for _ in range(repetitions):
        total_time += float(run_command(
            f"OMP_NUM_THREADS={num_threads} make -s clean run O={O_level} TASK_SIZE={task_size} EXECUTION={execution}").stdout.decode())
    return round(total_time/repetitions, 4)


def main():
    SIZES = [int(a) for a in [1e4, 1e5, 1e6]]
    NUMS_THREADS = [1, 2, 4, 8, 16, 32]
    O_LEVELS = [0, 1, 2, 3]
    TASK_SIZES = [50, 100, 200, 400, 800]
    N_REPETITIONS = 5

    for size in SIZES:
        generate_file(size)
        print(f"Size: {size}")
        for O_level in O_LEVELS:
            for task_size in TASK_SIZES:
                avg_time = make_measures(
                    1, O_level, task_size, N_REPETITIONS, "parallel")
                print(
                    f"avg_time for serial execution, O{O_level} optimization, task size {task_size} = {avg_time}")
                for num_threads in NUMS_THREADS:
                    avg_time = make_measures(
                        num_threads, O_level, task_size, N_REPETITIONS)
                    print(
                        f"avg_time for {num_threads} threads, O{O_level} optimization, task size {task_size} = {avg_time}")


if __name__ == "__main__":
    main()
