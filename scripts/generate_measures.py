#!/usr/bin/python3
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
from tqdm import tqdm
from generate_file import generate_file
import statistics as stats
from pathlib import Path
import csv
import shutil


def run_command(command):
    commands = ["bash", "-c", command]
    return subprocess.run(commands, capture_output=True)


def single_measure(num_threads, O_level, task_size, execution):
    return float(
        run_command(
            f"OMP_NUM_THREADS={num_threads} make -s clean run O={O_level} TASK_SIZE={task_size} EXECUTION={execution}")
        .stdout.decode()
    )


def avg_measure(num_threads, O_level, task_size, repetitions, execution="parallel"):
    measures = []
    for _ in tqdm(range(repetitions)):
        measures.append(single_measure(
            num_threads, O_level, task_size, execution))

    return round(stats.fmean(measures), 4), round(stats.stdev(measures), 4)


def print_progress(size, O_level, task_size, avg_time, std_time, num_threads=None):
    if num_threads is not None:
        return print(
            f"SIZE {size}, O{O_level} optimization, task size {task_size}, {num_threads} threads. AVG_TIME: {avg_time}, STD_TIME {std_time}\n")

    print(f"SIZE {size}, O{O_level} optimization, task size {task_size}, serial execution. AVG_TIME: {avg_time}, STD_TIME {std_time}\n")


def main():
    SIZES = [int(a) for a in [1e4, 1e5, 1e6]]
    NUMS_THREADS = [1, 2, 4, 8, 16, 32]
    O_LEVELS = [0, 1, 2, 3]
    TASK_SIZES = [50, 100, 200, 400, 800]
    N_REPETITIONS = 2
    MEASURES_DIR = 'measures'

    # TODO Refactor filesave
    shutil.rmtree(MEASURES_DIR)
    for size in SIZES:
        print(f"Generating file with random numbers for size {size}")
        generate_file(size)
        print()
        for O_level in O_LEVELS:
            for task_size in TASK_SIZES:
                dirname = f"{MEASURES_DIR}/SIZE_{size}/O{O_level}"
                Path(dirname).mkdir(parents=True, exist_ok=True)

                with open(f"{dirname}/TASKSIZE_{task_size}.csv", 'w', newline='') as csvfile:
                    writer = csv.writer(csvfile, delimiter=";")
                    fieldnames = ['execution', 'threads', 'time', 'std deviation', 'speedup', 'efficiency']
                    writer.writerow(fieldnames)

                    serial_avg_time, std_time = avg_measure(1, O_level, task_size, N_REPETITIONS, "serial")
                    print_progress(size, O_level, task_size, serial_avg_time, std_time)
                    writer.writerow(['serial', 1, serial_avg_time, std_time, 1, 1])
                    for num_threads in NUMS_THREADS:
                        avg_time, std_time = avg_measure(num_threads, O_level, task_size, N_REPETITIONS)
                        print_progress(size, O_level, task_size, avg_time, std_time, num_threads)
                        speedup = serial_avg_time/avg_time
                        efficiency = speedup/num_threads
                        writer.writerow(['parallel', num_threads, avg_time, std_time, round(speedup, 4), round(efficiency, 4)])


if __name__ == "__main__":
    main()
