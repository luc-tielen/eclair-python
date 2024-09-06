#!/bin/bash

# NOTE: invoke this script from the root directory

FIXTURE_DIR=./tests/fixtures

clang -fPIC -c -o ${FIXTURE_DIR}/path.o ${FIXTURE_DIR}/path.ll
clang -shared -o ${FIXTURE_DIR}/libpath.so ${FIXTURE_DIR}/path.o
