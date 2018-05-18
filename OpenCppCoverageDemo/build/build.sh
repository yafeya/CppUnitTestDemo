export CC=/usr/local/bin/gcc
export CXX=/usr/local/bin/g++

cmake .. -G "Unix Makefiles" -DCMAKE_BUILD_TYPE=Debug -DBINARY_BITS=64 -DPlatform=x64
