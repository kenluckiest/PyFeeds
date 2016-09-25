cmake_minimum_required(VERSION 2.8.3)
PROJECT (PyFeeds)
set(CMAKE_BINARY_DIR ${CMAKE_SOURCE_DIR}/bin)
set(LIBRARY_OUTPUT_PATH ${CMAKE_BINARY_DIR}/lib)
set(EXECUTABLE_OUTPUT_PATH ${CMAKE_BINARY_DIR})

FIND_PACKAGE(PythonInterp)
FIND_PACKAGE(PythonLibs)

LINK_LIBRARIES(${Boost_LIBRARIES} ${PYTHON_LIBRARIES}) # Deprecated but so convenient!
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -lpython2.7 -lboost_python -lboost_system")

set(HEADERS
        liblinear/linear.h
        liblinear/tron.h
        liblinear/blas/blas.h
        liblinear/blas/blasp.h
        configure.h
        DicMap.h
        Feats.h
        FeaturesSelection.h
        Machine.h
        StrMap.h
        SylMap.h)

set(SOURCES
        liblinear/linear.cpp
        liblinear/tron.cpp
        liblinear/blas/daxpy.c
        liblinear/blas/ddot.c
        liblinear/blas/dnrm2.c
        liblinear/blas/dscal.c
        DicMap.cpp
        Feats.cpp
        FeaturesSelection.cpp
        Machine.cpp
        StrMap.cpp
        SylMap.cpp
        learner.cpp
        tokenizer.cpp)

INCLUDE_DIRECTORIES(${Boost_INCLUDE_DIRS} ${PYTHON_INCLUDE_DIRS} liblinear/blas)
LINK_DIRECTORIES(${CMAKE_CURRENT_SOURCE_DIR} liblinear)

#ADD_LIBRARY(libraries STATIC ${HEADERS} ${SOURCES})
ADD_LIBRARY(DongDu SHARED ${HEADERS} ${SOURCES})
set (PROJECT_LINK_LIBS ${LIBRARY_OUTPUT_PATH}/libDongDu.so)


#ADD_EXECUTABLE(learner learner.cpp)
#TARGET_LINK_LIBRARIES(learner ${PROJECT_LINK_LIBS} ${Boost_LIBRARIES} ${PYTHON_LIBRARIES})
PYTHON_ADD_MODULE(tokenizer tokenizer.cpp)
#ADD_LIBRARY(tokenizer SHARED tokenizer.cpp)
#TARGET_LINK_LIBRARIES(tokenizer boost_python ${PROJECT_LINK_LIBS} ${Boost_LIBRARIES} ${PYTHON_LIBRARIES})
#FILE(COPY tokenizer.so DESTINATION .)