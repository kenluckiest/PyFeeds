cmake_minimum_required(VERSION 2.8.3)
FIND_PACKAGE(PythonInterp)
FIND_PACKAGE(PythonLibs)

#include_directories(/usr/include/python2.7)

INCLUDE_DIRECTORIES(${Boost_INCLUDE_DIRS} ${PYTHON_INCLUDE_DIRS})
LINK_LIBRARIES(${Boost_LIBRARIES} ${PYTHON_LIBRARIES}) # Deprecated but so convenient!
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -lpython2.7 -lboost_python")

set(SOURCE_FILES
    configure.h
    DicMap.cpp
    DicMap.h
    Feats.cpp
    Feats.h
    FeaturesSelection.cpp
    FeaturesSelection.h
    Machine.cpp
    Machine.h
    StrMap.cpp
    StrMap.h
    SylMap.cpp
    SylMap.h
    tokenizer.cpp)

PYTHON_ADD_MODULE(tokenizer tokenizer.cpp)
FILE(COPY test.py DESTINATION .)