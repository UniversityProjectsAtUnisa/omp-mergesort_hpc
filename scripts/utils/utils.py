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
import sys


def get_list_of_files(dirname):
    """Creates a list of paths to files in the directory dirname

    Args:
        dirname (str): the name of the directory to scan

    Returns:
        list of str: the list of paths to files in the directory
    """
    # creates a list of files and sub directories
    # names in the given directory
    listOfFile = os.listdir(dirname)

    allFiles = list()
    for entry in listOfFile:
        # creates full path
        fullPath = os.path.join(dirname, entry)
        # if it's a directory then get the list of files in this directory
        if os.path.isdir(fullPath):
            allFiles = allFiles + get_list_of_files(fullPath)
        else:
            # accumulates the filenames
            allFiles.append(fullPath)

    return allFiles


class HiddenErrors:
    """
    Context to hide error of wrapped functions and methods
    """
    def __enter__(self):
        self._original_stderr = sys.stderr
        sys.stderr = open(os.devnull, 'w')

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stderr.close()
        sys.stderr = self._original_stderr
