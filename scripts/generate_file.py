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


import argparse
import random
from tqdm import tqdm

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('N', metavar='N', type=int,
                    help='the amount of numbers to be generated')
parser.add_argument('--max', dest='max', default=2**31 - 1,
                    help='maximum number that can be generated')
parser.add_argument('--min', dest='min',
                    help="""minimum number that can be generated;
                    default: -max
                    """)
parser.add_argument('--input', dest='input', default="input/in.txt",
                    help="input file name")


def generate_file(N, min_value=None, max_value = 2**31 - 1, filename="input/in.txt"):
    min_value = min_value if min_value is not None else -max_value
    with open(filename, "w") as f:
        f.write(str(N)+"\n")
        for _ in tqdm(range(N)):
            r = random.randint(min_value, max_value)
            f.write(f"{r} ")


def main():
    N = parser.parse_args().N
    _max = parser.parse_args().max
    _min = parser.parse_args().min
    _input = parser.parse_args().input

    print(f"N: {N}, max: {_max}, min: {_min}, filename: {_input}")

    generate_file(N, _min, _max, _input)


if __name__ == "__main__":
    main()
