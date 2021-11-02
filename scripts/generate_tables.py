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

import os
from utils.utils import get_list_of_files, HiddenErrors
import pandas as pd
from pandas.plotting import table
import matplotlib.pyplot as plt
import dataframe_image as dfi
from functools import partial


# def main():
#     paths = get_list_of_files("measures")
#     pngs = filter(lambda p: os.path.splitext(p)[1] == ".png", paths)
#     csvs = filter(lambda p: os.path.splitext(p)[1] == ".csv", paths)
#     for path in pngs:
#         if os.path.splitext(path)[1] == ".png":
#             os.remove(path)

#     for path in csvs:
#         df = pd.read_csv(path, delimiter=";")

#         _, ax = plt.subplots(figsize=(12, 8))
#         ax = plt.subplot(111, frame_on=False)  # no visible frame
#         ax.xaxis.set_visible(False)  # hide the x axis
#         ax.yaxis.set_visible(False)  # hide the y axis
#         table(ax, df)  # where df is your data frame
#         plt.savefig(os.path.splitext(path)[0]+'.png', bbox_inches='tight')
#         plt.close()


def main():
    paths = get_list_of_files("measures")
    pngs = filter(lambda p: os.path.splitext(p)[1] == ".png", paths)
    for path in pngs:
        if os.path.splitext(path)[1] == ".png":
            os.remove(path)

    csvs = filter(lambda p: os.path.splitext(p)[1] == ".csv", paths)
    for path in csvs:
        df = pd.read_csv(path, delimiter=";")
        styled_df = df.style.hide_index()
        with HiddenErrors():
            dfi.export(styled_df, os.path.splitext(path)[0]+'.png', table_conversion="matplotlib", max_cols=6)


if __name__ == "__main__":
    main()
