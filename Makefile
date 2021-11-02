# Course: High Performance Computing 2020/2021
# 
# Lecturer: Francesco Moscato    fmoscato@unisa.it
# 
# Group: 
# De Stefano Alessandro   0622701470  a.destefano56@studenti.unisa.it
# Della Rocca Marco   0622701573  m.dellarocca22@studenti.unisa.it
# 
# OMP implementation of mergesort algorithm 
# Copyright (C) 2021 Alessandro De Stefano (EarendilTiwele) Marco Della Rocca (marco741)
# 
# This file is part of OMP Mergesort implementation.
# 
# OMP Mergesort implementation is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# OMP Mergesort implementation is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with OMP Mergesort implementation.  If not, see <http: //www.gnu.org/licenses/>.


# release is default, for debugging : make BUILD=debug
BUILD := release
flags.debug = -g -Wall
flags.release = -w

# parallel is default, for serial : make EXECUTION=serial
EXECUTION = parallel
OMP.parallel = -fopenmp
OMP.serial =
O := 0
TASK_SIZE := 100

# Wildcard to commands recipe
space := #
space +=
semicolon := ;

IDIR = include
SRCDIR = src
BUILDDIR = build
TESTDIR = test
EXECUTABLE = main.out

CC = gcc
OMP = ${OMP.${EXECUTION}}
CFLAGS = ${flags.${BUILD}} -I$(IDIR) $(OMP)
LDFLAGS = ${OMP.parallel}

TESTS = $(wildcard $(TESTDIR)/*.c)
TEST_OBJECTS = $(patsubst $(TESTDIR)/%.c,$(TESTDIR)/$(BUILDDIR)/%.o,$(TESTS))
TEST_EXECUTABLES = $(patsubst %.o,%.out,$(TEST_OBJECTS))
SOURCES = $(wildcard $(SRCDIR)/*.c)
OBJECTS = $(patsubst $(SRCDIR)/%.c,$(BUILDDIR)/%.o,$(SOURCES))
DEPS = $(wildcard $(IDIR)/*.h)

.PHONY: all
all: dir $(BUILDDIR)/$(EXECUTABLE) 

.PHONY: dir
dir:
	mkdir -p $(BUILDDIR)

.PHONY: test_dir
test_dir:
	mkdir -p $(TESTDIR)/$(BUILDDIR)

$(BUILDDIR)/$(EXECUTABLE): $(OBJECTS)
	$(CC) $^ -o $@ $(LDFLAGS) 

$(OBJECTS): $(BUILDDIR)/%.o: $(SRCDIR)/%.c $(DEPS)
	$(CC) -c -O$(O) $< -o $@ $(CFLAGS)

.PHONY: clean
clean:
	rm -f $(BUILDDIR)/*.o $(BUILDDIR)/$(EXECUTABLE) $(TESTDIR)/$(BUILDDIR)/*.o $(TESTDIR)/$(BUILDDIR)/*.out

.PHONY: run
run: dir $(BUILDDIR)/$(EXECUTABLE)
	$(BUILDDIR)/$(EXECUTABLE) $(TASK_SIZE)

# Run all tests
.PHONY: test
test: test_dir dir $(TEST_EXECUTABLES)
	$(subst $(space),$(semicolon),$(TEST_EXECUTABLES)) 

$(TEST_EXECUTABLES): $(TESTDIR)/$(BUILDDIR)/%.out: $(TESTDIR)/$(BUILDDIR)/%.o $(BUILDDIR)/%.o
	$(CC) $^ -o $@ $(LDFLAGS)

$(TESTDIR)/$(BUILDDIR)/%.o: $(TESTDIR)/%.c
	$(CC) -c -O2 $< -o $@ $(CFLAGS)

.PHONY: measures
measures:
	python3 scripts/generate_measures.py
	python3 scripts/generate_graphs.py
	python3 scripts/generate_tables.py