cmake_minimum_required(VERSION 2.6)

PROJECT(TestSourceCmake)

IF(UNIX)
    # use c++14 and static link for std c++ library
    SET(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++14 -static-libstdc++")
	IF(BINARY_BITS EQUAL 32)
        SET(CMAKE_C_FLAGS "${CMAKE_CXX_FLAGS} -m32")
		SET(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -m32")
    ENDIF()
ENDIF()

ADD_SUBDIRECTORY("TestSource"		"TestSource/bin")
ADD_SUBDIRECTORY("GoogleTest"		"GoogleTest/bin")
ADD_SUBDIRECTORY("UnitTestConsole"	"UnitTestConsole/bin")
