#!venv/bin/python3
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


'''
Script for generating speedup measures for different modes of execution
and different amount of threads
'''

import subprocess
from tqdm import tqdm
from generate_file import generate_file
import statistics as stats
from pathlib import Path
import csv
import shutil


def run_command(command):
    """Runs a command in bash synchronously

    Args:
        command (str): Command to run

    Returns:
        CompletedProcess: A process that has finished running.

        Attributes:
            args: The list or str args passed to run(). (["bash", "-c", command])
            returncode: The exit code of the process, negative for signals.
            stdout: The standard output
            stderr: The standard error
    """
    commands = ["bash", "-c", command]
    return subprocess.run(commands, capture_output=True)


def single_measure(num_threads, O_level, task_size, execution):
    """Measure the execution time for one run of the program with given parameters

    Args:
        num_threads (int): the number of threads
        O_level (int): the level of gcc optimization while compiling
        task_size (int): the maximum dimension of the array that can be processed by a single thread
        execution (str): the type of execution. Valid values are serial, parallel

    Returns:
        float: The execution time
    """
    return float(
        run_command(
            f"OMP_NUM_THREADS={num_threads} make -s clean run O={O_level} TASK_SIZE={task_size} EXECUTION={execution}")
        .stdout.decode()
    )


def avg_measure(num_threads, O_level, task_size, repetitions, execution="parallel"):
    """Measure the average execution time and the standard deviation for repetitions runs of the program with given parameters

    Args:
        num_threads (int): the number of threads
        O_level (int): the level of gcc optimization while compiling
        task_size (int): the maximum dimension of the array that can be processed by a single thread
        repetitions (int): the number of times to execute the measurement
        execution (str, optional): the type of execution. Valid values are serial, parallel. Defaults to "parallel".

    Returns:
        (float, float): (avg_time, std_time)

        Attributes:
            avg_time: the average time
            std_time: the standard deviation 
    """
    measures = []
    for _ in tqdm(range(repetitions)):
        measures.append(single_measure(
            num_threads, O_level, task_size, execution))

    return round(stats.fmean(measures), 4), round(stats.stdev(measures), 4)


def print_progress(size, O_level, task_size, avg_time, std_time, num_threads=None):
    """Utility print of the progress

    Args:
        size (int): the amount of data in the input file
        O_level (int): the level of gcc optimization while compiling
        task_size (int): the maximum dimension of the array that can be processed by a single thread
        avg_time (float): the average execution time
        std_time (float): the standard deviation for the execution time
        num_threads (int, optional): the number of threads. If it's None it assumes the execution to have been serial. Defaults to None.
    """
    if num_threads is not None:
        return print(
            f"SIZE {size}, O{O_level} optimization, task size {task_size}, {num_threads} threads. AVG_TIME: {avg_time}, STD_TIME {std_time}\n")

    print(f"SIZE {size}, O{O_level} optimization, task size {task_size}, serial execution. AVG_TIME: {avg_time}, STD_TIME {std_time}\n")


def write_table(header, rows, path):
    """Exports the data in header and rows in a csv file in path location

    Args:
        header (list of str): the names of the columns
        rows (list of list): the data to be exported
        path (str): the path for the output csv file
    """

    # Creates the parent folder if doesn't exist
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, 'w', newline='') as csvfile:
        # Uses semicolon delimiter for Microsoft Excel compatibility
        writer = csv.writer(csvfile, delimiter=";")
        writer.writerow(header)
        writer.writerows(rows)


def main():
    SIZES = [int(a) for a in [1e5, 4e5, 16e5]]
    NUMS_THREADS = [1, 2, 4, 8, 16, 32]
    O_LEVELS = [0, 1, 2, 3]
    TASK_SIZES = [1, 50, 100, 200, 400, 800]
    N_REPETITIONS = 10
    MEASURES_DIR = 'measures'
    fieldnames = ['execution', 'threads', 'time', 'stdev', 'speedup', 'efficiency']

    # Deletes every old measure (graphs and tables included)
    shutil.rmtree(MEASURES_DIR, ignore_errors=True)
    for size in SIZES:
        print(f"Generating file with random numbers for size {size}")
        generate_file(size)
        print()
        for O_level in O_LEVELS:
            for task_size in TASK_SIZES:
                rows, path = [], f"{MEASURES_DIR}/SIZE_{size}/O{O_level}/TASKSIZE_{task_size}.csv"

                # Runs a serial execution
                serial_avg_time, std_time = avg_measure(1, O_level, task_size, N_REPETITIONS, "serial")
                print_progress(size, O_level, task_size, serial_avg_time, std_time)
                rows.append(['serial', 1, serial_avg_time, std_time, 1, 1])

                # Runs parallels executions
                for num_threads in NUMS_THREADS:
                    avg_time, std_time = avg_measure(num_threads, O_level, task_size, N_REPETITIONS)
                    print_progress(size, O_level, task_size, avg_time, std_time, num_threads)
                    speedup = serial_avg_time/avg_time
                    efficiency = speedup/num_threads
                    rows.append(['parallel', num_threads, avg_time, std_time, round(speedup, 4), round(efficiency, 4)])

                # Save results in csv file
                write_table(fieldnames, rows, path)


if __name__ == "__main__":
    main()
