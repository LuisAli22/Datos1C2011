#!/bin/bash
swig -c++ -python -shadow Buffer.i
if [ ! "$?" = 0 ]; then
	exit 0
fi
g++ -fPIC -c -I/usr/include/python2.6 \Buffer.cpp Buffer_wrap.cxx
if [ ! "$?" = 0 ]; then
	exit 0
fi
g++ -shared  Buffer.o Buffer_wrap.o -o _Buffer.so
