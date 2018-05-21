#!/bin/bash
ROOT_DIR=${PWD};
rm -rf  OpenCppCoverageDemo/cmake/x*
rm -rf  OpenCppCoverageDemo/cmake/reports
cd OpenCppCoverageDemo/cmake/
./build.sh
cd x64/debug/
make
#make TestSource_coverage
#cd $ROOT_DIR
#./OpenCppCoverageDemo/cmake/x64/debug/UnitTestConsole/bin/UnitTestConsole
#sonar-scanner
