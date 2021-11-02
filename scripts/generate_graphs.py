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

from matplotlib import pyplot as plt
import numpy as np
import os
import csv
from utils.utils import get_list_of_files


def plot_from_table(table, save=True, name="", show_plot=False):
    if save and not name:
        raise Exception("No filename to save file")

    x, y = [0], [0]
    thread_pos = table[0].index("threads")
    speedup_pos = table[0].index("speedup")
    for row in table[2:]:
        x.append(row[thread_pos])
        y.append(row[speedup_pos])

    _, ax = plt.subplots(figsize=(12, 8))
    y = list(map(float, y))
    ax.plot(x, y, 'ro-', label='Experimental')
    ax.plot(x, x, color='blue', label='Ideal')
    plt.style.use('seaborn-whitegrid')

    plt.autoscale(enable=True, axis='x', tight=True)
    plt.autoscale(enable=True, axis='y', tight=True)

    plt.legend()
    plt.xlabel("Processors")
    plt.ylabel("Speedup")
    if show_plot:
        plt.show()
    if save:
        plt.savefig(name)
    plt.close()


def main():
    paths = get_list_of_files("measures")
    jpgs = filter(lambda p: os.path.splitext(p)[1] == ".jpg", paths)
    for path in jpgs:
        if os.path.splitext(path)[1] == ".jpg":
            os.remove(path)

    csvs = filter(lambda p: os.path.splitext(p)[1] == ".csv", paths)
    for path in csvs:
        with open(path, newline="") as csvfile:
            table = csv.reader(csvfile, delimiter=";")
            plot_from_table(list(table), name=os.path.splitext(path)[0]+'.jpg')


if __name__ == "__main__":
    main()
