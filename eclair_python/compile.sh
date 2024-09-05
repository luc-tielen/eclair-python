#!/bin/bash

clang -fPIC -c -o add.o add.c
clang -shared -o libcadd.so add.o
