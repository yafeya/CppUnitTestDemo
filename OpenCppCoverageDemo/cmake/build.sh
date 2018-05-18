#!/bin/bash

CURRENT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# make sure gcc 4.9.2 or higher version was installed in /usr/local/bin
export CC=/usr/local/bin/gcc
export CXX=/usr/local/bin/g++

mkdir -p ${CURRENT_DIR}/x64/debug
mkdir -p ${CURRENT_DIR}/x86/debug
mkdir -p ${CURRENT_DIR}/x64/release
mkdir -p ${CURRENT_DIR}/x86/release

#build 64bit
cd ${CURRENT_DIR}/x64/debug
cmake ../../.. -G "Unix Makefiles" -DCMAKE_BUILD_TYPE=Debug -DBINARY_BITS=64 -DPlatform=x64 -DCMAKE_INSTALL_PREFIX=${CURRENT_DIR}/../build_linux
cd ${CURRENT_DIR}/x64/release
cmake ../../.. -G "Unix Makefiles" -DCMAKE_BUILD_TYPE=Release -DBINARY_BITS=64 -DPlatform=x64 -DCMAKE_INSTALL_PREFIX=${CURRENT_DIR}/../build_linux

# build 32bit
# TODO: use toolchain file or set compile/link flags to specify -m32?
# for now, just set compile/link flags to set -m32 in top level cmake file
cd ${CURRENT_DIR}/x86/debug
cmake ../../.. -G "Unix Makefiles" -DCMAKE_BUILD_TYPE=Debug -DBINARY_BITS=32 -DPlatform=x86 -DCMAKE_INSTALL_PREFIX=${CURRENT_DIR}/../build_linux
cd ${CURRENT_DIR}/x86/release
cmake ../../.. -G "Unix Makefiles" -DCMAKE_BUILD_TYPE=Release -DBINARY_BITS=32 -DPlatform=x86 -DCMAKE_INSTALL_PREFIX=${CURRENT_DIR}/../build_linux
