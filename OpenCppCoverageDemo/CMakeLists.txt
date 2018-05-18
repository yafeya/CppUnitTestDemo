cmake_minimum_required(VERSION 2.6)

PROJECT(TestSourceCmake)

IF(UNIX)

    SET(CMAKE_MODULE_PATH ${PROJECT_SOURCE_DIR}/CMakeModules)

    # use c++14 and static link for std c++ library
    SET(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++14 -static-libstdc++")
	IF(BINARY_BITS EQUAL 32)
        SET(CMAKE_C_FLAGS "${CMAKE_CXX_FLAGS} -m32")
		SET(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -m32")
    ENDIF()

    IF(CMAKE_COMPILER_IS_GNUCXX)
      INCLUDE(CodeCoverage)
      APPEND_COVERAGE_COMPILER_FLAGS()
      setup_target_for_coverage(NAME TestSource_coverage
                                EXECUTABLE UnitTestConsole
                                EXECUTABLE_ARGS --gtest_output=xml:./${PROJECT_BUILD_DIR}/reports/gtest_report.xml
                                DEPENDENCIES UnitTestConsole)
     ENDIF()

ENDIF()

ADD_SUBDIRECTORY("TestSource"		"TestSource/bin")
ADD_SUBDIRECTORY("GoogleTest"		"GoogleTest/bin")
ADD_SUBDIRECTORY("UnitTestConsole"	"UnitTestConsole/bin")
