cmake_minimum_required(VERSION 3.16)
project(satlike_graduate)

set(CMAKE_CXX_STANDARD 14)

add_executable(satlike_graduate pms.cpp pms.h deci.h heuristic.h basis_pms.h build.h)